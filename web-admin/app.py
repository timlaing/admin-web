# -*- coding: utf-8 -*-
"""Main Application entry point"""
from importlib import import_module

from flask import Flask

app = Flask(__name__)
app.config["modules"] = []

with app.app_context():
    print(__package__, "views")
    import_module(name=f"{__package__}.views")
