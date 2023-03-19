# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Coroutine, Dict, List, Protocol, TypeVar

if TYPE_CHECKING:
    T = TypeVar("T")
    Coro = Coroutine[Any, Any, T]
    CoroFunc = Callable[..., Coro[Any]]

    BotT = TypeVar("BotT", bound="SupportsListeners")

    class SupportsListeners(Protocol):
        extra_events: Dict[str, List[CoroFunc]]

        def dispatch(self: Any, event_name: str, *args: Any, **kwargs: Any) -> None:
            ...
