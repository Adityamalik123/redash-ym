from functools import wraps
from flask import g, request, Response
from typing import List
import requests
from redash import settings

def user():
    def wrap(f):
        def decorated_function(*args, **kwargs):
            if 'ym_xid' in request.cookies:
                token = request.cookies["ym_xid"]
            elif 'x-auth-token' in request.headers:
                token = request.headers["x-auth-token"]
            else:
                return "Access denied"

            url = settings.SSO_URL + '/session'
            headers = {'x-auth-token': token, 'x-auth-cookie': "true"}
            r = requests.get(url, headers=headers)
            g.user = r.json()["session"]
            g.auth_token = token

            return f(*args, **kwargs)

        return decorated_function
    return wrap


def bot(roles:List):
    def wrap(f):
        def decorated_function(*args, **kwargs):
            if 'ym_xid' in request.cookies:
                token = request.cookies["ym_xid"]
            elif 'x-auth-token' in request.headers:
                token = request.headers["x-auth-token"]
            else:
                return Response(status=401)
            g.auth_token = token

            url = settings.SSO_URL+'/session'
            headers = {'x-auth-token': token, 'x-auth-cookie': "true"}
            r = requests.get(url, headers=headers)
            if "session" not in r.json().keys():
                return Response(status=401)
            g.user = r.json()["session"]
            # if r.headers['Set-Cookie']:
            #     g.cookie=r.headers['Set-Cookie']
            bot_id = request.args.get('bot')
            if bot_id is None:
                if "bot" in request.cookies:
                    bot_id = request.cookies['bot']

            if bot_id is not None:
                for role in g.user["roles"]:
                    if bot_id == role["owner"] and role["role"] in roles:
                        g.bot = bot_id
                        break

            return f(*args, **kwargs)
        return decorated_function
    return wrap
