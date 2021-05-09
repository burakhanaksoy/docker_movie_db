# -*- coding: utf-8 -*-

import os
from os.path import join


def _script_path():
    """Returns the path to the dir this script is in"""
    return os.path.dirname(os.path.realpath(__file__))


class path(object):
    """Class of paths to GCC"""

    @staticmethod
    def bin():
        return join(_script_path(), "gcc_root", "bin")

    @staticmethod
    def lib():
        return join(_script_path(), "gcc_root", "lib")

    @staticmethod
    def gcc():
        return join(path.bin(), "gcc")
