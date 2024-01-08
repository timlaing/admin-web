# -*- coding: utf-8 -*-
"""Module to handle DNS functionality"""
from flask import render_template
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from ._base import Module


@Module("DNS", "/dns/zones/", "dns_zones")
class DnsZoneView(MethodView):
    """View for listing DNS Zones"""

    def get(self) -> ResponseReturnValue:
        """Lists the DNS Zones"""
        return render_template("dns.html")
