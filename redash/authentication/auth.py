from functools import wraps
from flask import g, request, Response
from typing import List, Dict,Any
import requests
import os
import configparser
import config

configuration = {}
environment = os.environ.get('ML_ENV','production')
sso = ''
if environment.lower() == 'production':
    configuration = config.ProductionConfig()
    sso = configuration.ML_SSO_URL
elif environment.lower() == 'deployment':
    configuration = configparser.ConfigParser()
    configuration.read('/root/.config/configstore/ml.ini')
    sso = configuration.get('CONFIG','ML_SSO_URL')


def check_auth(username:str, password:str)->bool:
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'c0mpl1cat3d'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response('Could not verify your access level for that URL.\n You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def user():
    def wrap(f):
        def decorated_function(*args, **kwargs):
            if 'ym_xid' in request.cookies:
                token = request.cookies["ym_xid"]
            elif 'x-auth-token' in request.headers:
                token = request.headers["x-auth-token"]
            else:
                return "Access denied"

            url = sso + '/session'
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

            url = sso+'/session'
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
