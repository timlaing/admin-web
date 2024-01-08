"""Module to handle DNS functionality"""
from flask import current_app as app
from flask.typing import ResponseReturnValue
from flask.views import View


class DnsZoneView(View):
    """View for listing DNS Zones"""

    def dispatch_request(self) -> ResponseReturnValue:
        return self.list_zones()

    def list_zones(self) -> ResponseReturnValue:
        """Lists the DNS Zones"""
        return ""


app.config["modules"].append({"name": "dns", "class": DnsZoneView})
app.add_url_rule("/dns/zones/", view_func=DnsZoneView.as_view("dns_zones"))
