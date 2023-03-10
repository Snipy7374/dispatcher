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
    List,
    Callable,
    TypeVar,
    Any,
    Coroutine,
    Mapping,
    TYPE_CHECKING
)

import logging
import types

if TYPE_CHECKING:
    from .types import AnyBot


__all__ = ("Dispatcher",)

_log = logging.getLogger(__name__)

T = TypeVar("T")
Coro = Coroutine[Any, Any, T]
CoroFunc = Callable[..., Coro[Any]]


class Dispatcher:
    """
    A class to handles custom event dispatching.

    .. versionadded:: 0.0.1

    Parameters
    ----------
    bot: AnyBot
    library_name: :class:`str`
        The name of the library that you're using. The ``library_name`` must be one of the
        supported library.
    
    Raises
    ------
    NotImplemented
        The ``library_name`` is not supported.
    """

    def __init__(self, bot: AnyBot, library_name: str = "disnake") -> None:
        self.bot = bot

    @property
    def listeners(self) -> Mapping[str, List[CoroFunc]]:
        """Mapping[:class:`str`, List[Callable]]: A read-only mapping of event name to listeners.

        .. versionadded:: 0.0.1
        """
        from .types import supported_bots

        if isinstance(self.bot, supported_bots):
            return types.MappingProxyType(self.bot.extra_events)  # type: ignore

        # self.bot is either Client or AutoSharededClient
        # these can't have listeners
        return {}

    def dispatch(self, event: str, *args, **kwargs) -> None:
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

        Raises
        ------
        ValueError
            ``event`` is not of :class:`str` type.
        """
        if not isinstance(event, str):
            raise ValueError(f"event must be of str type, not {event.__class__!r}")

        self.bot.dispatch(event, *args, **kwargs)
        _log.info("%s event was dispatched", event)