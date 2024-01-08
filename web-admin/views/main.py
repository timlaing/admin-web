# -*- coding: utf-8 -*-
"""Module to handle home page functionality"""
from flask import current_app as app
from flask import render_template
from flask.typing import ResponseReturnValue
from flask.views import View


class HomeView(View):
    """View for listing home page"""

    def dispatch_request(self) -> ResponseReturnValue:
        return self.list_modules()

    def list_modules(self) -> ResponseReturnValue:
        """Lists the modules"""
        return render_template("home.html", modules=app.config["modules"])


app.add_url_rule("/", view_func=HomeView.as_view("home"))
