# -*- coding: utf-8 -*-
"""Module to handle home page functionality"""
from flask import current_app as app
from flask import render_template
from flask.typing import ResponseReturnValue

from ..utils.decorators import module_view
from ..utils.views import BaseModuleView


@module_view("/")
class HomeView(BaseModuleView):  # pylint: disable=too-few-public-methods
    """View for listing home page"""

    name = "Home"
    view_name = "home"

    def get(self) -> ResponseReturnValue:
        """Lists the modules"""
        return render_template("home.html", modules=app.config["modules"])
