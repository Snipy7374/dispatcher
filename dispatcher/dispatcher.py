"""
MIT License

Copyright (c) 2023 Snipy7374

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations
from typing import (
    Any,
    Generic,
    List,
    Mapping,
    TYPE_CHECKING,
)

import logging
import types

if TYPE_CHECKING:
    from .types import CoroFunc, BotT

__all__ = ("Dispatcher",)

_log = logging.getLogger(__name__)

class Dispatcher(Generic[BotT]):
    """
    A class to handles custom event dispatching.

    .. versionadded:: 0.0.1

    Parameters
    ----------
    bot: BotT
        The bot instance to work with.
    """

    def __init__(self, bot: BotT) -> None:
        self.bot = bot

    @property
    def listeners(self) -> Mapping[str, List[CoroFunc]]:
        """Mapping[:class:`str`, List[Callable]]: A read-only mapping of event name to listeners.

        .. versionadded:: 0.0.1
        """
        if hasattr(self.bot, "extra_events"):
            return types.MappingProxyType(self.bot.extra_events)

        # self.bot is either Client or AutoShardedClient
        # these can't have listeners
        return {}

    def dispatch(self, event: str, *args: Any, **kwargs: Any) -> None:
        """A function to dispatch custom events.

        .. versionadded:: 0.0.1

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
        """
        self.bot.dispatch(event, *args, **kwargs)
        _log.info("%s event was dispatched", event)