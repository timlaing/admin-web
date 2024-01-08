# -*- coding: utf-8 -*-
"""Module to handle home page functionality"""
from flask import current_app as app
from flask import render_template
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from ._base import Module


@Module("Home", "/", "home", hide=True)
class HomeView(MethodView):
    """View for listing home page"""

    def get(self) -> ResponseReturnValue:
        """Lists the modules"""
        return render_template("home.html", modules=app.config["modules"])
