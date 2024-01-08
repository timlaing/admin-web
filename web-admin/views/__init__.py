# -*- coding: utf-8 -*-
"""Module loader"""
import glob
import os
from importlib import import_module

module_files = glob.glob(f"{__path__[0]}/[A-Za-z]*.py")

for module_file in module_files:
    filename = os.path.basename(module_file)
    module, _ = os.path.splitext(filename)
    print(__package__, module)
    import_module(name=f"{__package__}.{module}")
