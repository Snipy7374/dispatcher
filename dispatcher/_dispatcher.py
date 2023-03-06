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

from .generator import Generator

_log = logging.getLogger(__name__)

T = TypeVar("T")
Coro = Coroutine[Any, Any, T]
CoroFunc = Callable[..., Coro[Any]]

SUPPORTED_LIBRARIES = (
    "disnake",
    "nextcord",
    "pycord",
    "discord",
)


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
        if library_name not in SUPPORTED_LIBRARIES:
            raise NotImplemented(f"unsupported library: {library_name!r}")
        self.library_name = library_name
        self._generator = Generator(library=library_name)
        self._generator._generate_types()
    
    @property
    def listeners(self) -> Mapping  [str, List[CoroFunc]]:
        """Mapping[:class:`str`, List[Callable]]: A read-only mapping of event name to listeners.
        
        .. versionadded:: 0.0.1
        """
        # hacky way
        from .types import Bot, AutoShardedBot

        # btw disnake is better
        # importing thins that does not exist on other forks but that exist on disnake 
        if self.library_name == "disnake":
            from .types import InteractionBot, AutoShardedInteractionBot  # type: ignore
            if isinstance(self.bot, (Bot, AutoShardedBot, InteractionBot, AutoShardedInteractionBot)):
                return types.MappingProxyType(self.bot.extra_events)  # type: ignore
        
        if isinstance(self.bot, (Bot, AutoShardedBot)):
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