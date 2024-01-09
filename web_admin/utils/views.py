# -*- coding: utf-8 -*-
"""Base view code"""
from abc import ABCMeta, abstractmethod

from flask.views import MethodView


class BaseModuleView(MethodView, metaclass=ABCMeta):
    """Sub module information"""

    hide = True
    _sub_modules: list[MethodView] = []

    @classmethod
    @property
    @abstractmethod
    def view_name(cls):
        """The view name"""

    @classmethod
    @property
    @abstractmethod
    def name(cls):
        """The display name"""

    @classmethod
    @property
    def sub_modules(cls) -> list[MethodView]:
        """Return The list of sub_modules to use"""
        print(cls)

        return cls._sub_modules


class ModuleView(BaseModuleView, metaclass=ABCMeta):
    """Base class for module view"""

    hide = False

    @classmethod
    @property
    @abstractmethod
    def description(cls):
        """The display description"""

    @classmethod
    @property
    @abstractmethod
    def icon(cls):
        """The icon to use"""
