# -*- coding: utf-8 -*-
"""Module to handle DNS functionality"""
from flask import render_template
from flask.typing import ResponseReturnValue

from ..utils.decorators import module_view, parent_view
from ..utils.views import BaseModuleView, ModuleView


@module_view("/dns/")
class DnsView(ModuleView):  # pylint: disable=too-few-public-methods
    """View for listing DNS Zones"""

    name = "DNS"
    view_name = "dns"
    icon = "#collection"
    description = "Management of DNS functionality."

    def get(self) -> ResponseReturnValue:
        """Lists the DNS Zones"""
        return render_template("dns.html")


@parent_view(DnsView)
@module_view("/dns/zones/")
class ZoneView(BaseModuleView):
    """View the zones"""

    name = "Zones"
    view_name = "dns_zones"


@parent_view(DnsView)
@module_view("/dns/records/")
class RecordView(BaseModuleView):
    """View the records"""

    name = "Records"
    view_name = "dns_records"
