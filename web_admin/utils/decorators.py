# -*- coding: utf-8 -*-
"""Decorator helpers"""
from flask import current_app as app

from .views import BaseModuleView


class module_view:  # pylint: disable=invalid-name,too-few-public-methods
    """decorator for module views"""

    def __init__(self, route: str, hide=False):
        self._route = route
        self._hide = hide

    def __call__(self, cls: BaseModuleView) -> BaseModuleView:
        cls.route = self._route
        cls.hide = self._hide or cls.hide
        cls.sub_modules = []

        app.add_url_rule(
            self._route,
            view_func=cls.as_view(cls.view_name),
        )

        if not (self._hide or cls.hide):
            app.config["modules"].append(cls)

        return cls


class parent_view:  # pylint: disable=invalid-name,too-few-public-methods
    """decorator for client views"""

    def __init__(self, parent: BaseModuleView):
        self._parent = parent

    def __call__(self, cls: BaseModuleView) -> BaseModuleView:
        self._parent.sub_modules.append(cls)
        return cls
