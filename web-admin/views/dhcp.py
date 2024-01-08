# -*- coding: utf-8 -*-
"""Module to handle DHCP functionality"""
from flask import render_template
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from ._base import Module


@Module("DHCP", "/dhcp/leases/", "dhcp_leases")
class DHCPLeaseView(MethodView):
    """View for listing DHCP Leases"""

    def get(self) -> ResponseReturnValue:
        """Lists the DHCP leases"""
        return render_template("dhcp.html")
