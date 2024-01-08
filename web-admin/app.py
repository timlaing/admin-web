# -*- coding: utf-8 -*-
"""Main Application entry point"""
from flask import Flask

app = Flask(__name__)
app.config["modules"] = []

with app.app_context():
    from . import views
