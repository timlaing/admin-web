# -*- coding: utf-8 -*-
"""Module to handle DHCP functionality"""
from flask import render_template
from flask.typing import ResponseReturnValue

from ..utils.decorators import module_view, parent_view
from ..utils.views import BaseModuleView, ModuleView


@module_view("/dhcp/")
class DHCPView(ModuleView):  # pylint: disable=too-few-public-methods
    """View for listing DHC"""

    name = "DHCP"
    view_name = "dhcp"
    icon = "#collection"
    description = "Management of DHCP functionality."

    def get(self) -> ResponseReturnValue:
        """Lists the DHCP modules"""
        return render_template("dhcp.html")


@parent_view(DHCPView)
@module_view("/dhcp/reservations/")
class ReservationView(BaseModuleView):
    """View the reservations"""

    name = "Reservations"
    view_name = "dhcp_reservations"


@parent_view(DHCPView)
@module_view("/dhcp/pools/")
class PoolView(BaseModuleView):
    """View the pools"""

    name = "Pools / Subnets"
    view_name = "dhcp_pools"


@parent_view(DHCPView)
@module_view("/dhcp/leases/")
class LeaseView(BaseModuleView):
    """View the leases"""

    name = "Leases"
    view_name = "dhcp_leases"
