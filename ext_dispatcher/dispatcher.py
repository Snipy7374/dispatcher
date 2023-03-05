from __future__ import annotations
from typing import TYPE_CHECKING

import logging

if TYPE_CHECKING:
    from .types import AnyBot  # type: ignore


from .generator import Generator

_log = logging.getLogger(__name__)


class Dispatcher:
    """
    """
    def __init__(self, bot: AnyBot, library_name: str = "disnake") -> None:
        self.bot = bot
        self.library_name = library_name
        self._generator = Generator(library=library_name)
        self._generator._generate_types()
    
    @property
    def get_listeners(self):
        self.bot.extra_events

    def dispatch(self, event: str, *args, **kwargs) -> None:
        """
        Parameters
        ----------
        event: :class:`str`
            The name of the event that should be dispatched.
        *args
            Positional arguments that a callback listening for this
            ``event`` must take.
        **kwargs
            Keyword arguments that a callback listening for this ``event``
            must take.

        Raises
        ------
        ValueError
            ``event`` is not of :class:`str` type.
        """
        if not isinstance(event, str):
            raise ValueError(f"event must be of str type, not {event.__class__!r}")

        self.bot.dispatch(event, *args, **kwargs)
        _log.info("%s event was dispatched", event)