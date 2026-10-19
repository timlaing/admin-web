# -*- coding: utf-8 -*-
"""Main Application entry point"""

from importlib import import_module

from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["modules"] = []

# Guard state-changing requests (POST/PUT/PATCH/DELETE) against cross-site
# request forgery. Every view is GET today, so nothing breaks by switching this
# on now: it closes the Sonar python:S4502 finding ahead of the DHCP/DNS/RADIUS
# write endpoints rather than after them. SECRET_KEY must be configured before
# the first POST endpoint lands, or Flask-WTF refuses to mint tokens.
csrf = CSRFProtect(app)

with app.app_context():
    print(__package__, "views")
    import_module(name=f"{__package__}.views")
