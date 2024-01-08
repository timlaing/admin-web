# -*- coding: utf-8 -*-
"""Module to handle Radius functionality"""
from flask import render_template
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from ._base import Module


@Module("Radius", "/radius/users/", "radius_users")
class RadiusUsersView(MethodView):  # pylint: disable=too-few-public-methods
    """View for listing Radius Users"""

    def get(self) -> ResponseReturnValue:
        """Lists the Radius Users"""
        return render_template("radius.html")
