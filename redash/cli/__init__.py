import click
import simplejson
from flask import current_app
from flask.cli import FlaskGroup, run_command

from redash import create_app
from redash.cli import rq
from redash.monitor import get_status


def create(group):
    app = current_app or create_app()
    group.app = app

    @app.shell_context_processor
    def shell_context():
        from redash import models, settings

        return {"models": models, "settings": settings}

    return app


@click.group(cls=FlaskGroup, create_app=create)
def manager():
    """Management script for Redash"""

manager.add_command(rq.manager, "rq")
manager.add_command(run_command, "runserver")


@manager.command()
def status():
    print(simplejson.dumps(get_status(), indent=2))
