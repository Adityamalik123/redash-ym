#!/usr/bin/env python
"""
CLI to manage redash.
"""
from flask import current_app
from redash import create_app
if __name__ == '__main__':
    app = current_app or create_app()
    app.run(debug=True)
