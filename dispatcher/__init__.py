"""Dispatcher for discord.py and forks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A basic event dispatcher for the discord.py wrapper
and forks.

The supported libraries are:
    - discord.py
    - disnake
    - nextcord
    - pycord

This library could work for other discord.py forks but the type
annotation won't work.

:copyright: (c) 2023-present Snipy7374
:license: MIT, see LICENSE for more details.
"""

__name__ = "dispatcher"
__author__ = "Snipy7374"
__copyright__ = "Copyright 2023-present Snipy7374"
__license__ = "MIT"
__version__ = "0.0.1"


from ._dispatcher import *
from .enums import *
