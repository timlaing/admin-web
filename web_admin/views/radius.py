# -*- coding: utf-8 -*-
"""Module to handle Radius functionality"""
from flask import render_template
from flask.typing import ResponseReturnValue

from ..utils.decorators import module_view, parent_view
from ..utils.views import BaseModuleView, ModuleView


@module_view("/radius/")
class RadiusView(ModuleView):  # pylint: disable=too-few-public-methods
    """View for listing Radius Users"""

    name = "Radius"
    view_name = "radius"
    icon = "#collection"
    description = "Management of Network authentication."

    def get(self) -> ResponseReturnValue:
        """Lists the Radius Users"""
        return render_template("radius.html")


@parent_view(RadiusView)
@module_view("/radius/users/")
class UsersView(BaseModuleView):
    """View the reservations"""

    name = "Users"
    view_name = "radius_users"


@parent_view(RadiusView)
@module_view("/radius/computers/")
class ComputerView(BaseModuleView):
    """View the computer accounts"""

    name = "Computer Accounts"
    view_name = "radius_computer"


@parent_view(RadiusView)
@module_view("/radius/server/")
class ServerView(BaseModuleView):
    """View the server"""

    name = "Authentication Servers"
    view_name = "radius_servers"
