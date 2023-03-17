# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Coroutine, Dict, List, Protocol, Tuple, TypeVar

if TYPE_CHECKING:
    T = TypeVar("T")
    Coro = Coroutine[Any, Any, T]
    CoroFunc = Callable[..., Coro[Any]]

    BotT = TypeVar("BotT", bound="SupportsListeners")

    class SupportsListeners(Protocol):
        extra_events: Dict[str, List[CoroFunc]]
        dispatch: Callable[[Any, str, Tuple[Any], Dict[str, Any]], None]
