#!/usr/bin/env python3

"""Starts a web server that provides a pantry tracking web app."""

__author__ = "Garrett Heath Koller"
__copyright__ = "Copyright 2019, Garrett Heath Koller"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Garrett Heath Koller"
__email__ = "garrettheath4@gmail.com"
__status__ = "Prototype"

from .basehandler import run as start
from .requestrouter import RequestRouter

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        start(handler_class=RequestRouter, port=int(argv[1]))
    else:
        start(handler_class=RequestRouter, port=3000)
