# -*- coding: utf-8 -*-
"""Base view code"""
from flask import current_app as app
from flask.views import MethodView


class Module:  # pylint: disable=too-few-public-methods
    """Module decorator"""

    def __init__(
        self, name: str, route: str, view_name: str, *, hide: bool = False
    ) -> None:
        """Save the parameters"""
        self._name = name
        self._route = route
        self._view_name = view_name
        self._hide = hide

    def __call__(self, module: MethodView) -> None:
        """Register the class view"""
        app.add_url_rule(
            self._route,
            view_func=module.as_view(self._view_name),
        )

        if not self._hide:
            app.config["modules"].append(
                {
                    "name": self._name,
                    "view": self._view_name,
                    "description": "None",
                }
            )
