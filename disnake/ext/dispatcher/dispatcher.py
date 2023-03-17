# SPDX-License-Identifier: MIT

from __future__ import annotations

import logging
import types
from typing import TYPE_CHECKING, Any, Generic, List, Mapping

if TYPE_CHECKING:
    from .types import BotT, CoroFunc

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

    bot: BotT

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
