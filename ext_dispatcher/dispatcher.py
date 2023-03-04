from __future__ import annotations
from typing import Any, TYPE_CHECKING
from typing_extensions import TypeAlias

import os
import logging

if TYPE_CHECKING:
    from .types import AnyBot


from .generator import Generator

_log = logging.getLogger(__name__)


class Dispatcher:
    def __init__(self, bot: AnyBot, library_name: str = "disnake") -> None:
        self.bot = bot
        self.library_name = library_name
        self._generator = Generator(library=library_name)
        self._generator._generate_types()

    def dispatch(self, event: str, *args, **kwargs) -> None:
        self.bot.dispatch(event, *args, **kwargs)
        _log.info("%s event was dispatched", event)