# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Union, List
import typing

from pkg_resources import (  # type: ignore
    DistributionNotFound,
    get_distribution,
)

from sys import version_info as py_ver

from .errors import MultipleCompatibleLibraries, NoCompatibleLibraries

__all__ = (
    "supported_bots",
)

libraries = ("disnake", "nextcord", "py-cord", "discord.py", "discord")
found: List[str] = []


for library in libraries:
    try:
        get_distribution(library)
    except DistributionNotFound:
        pass
    else:
        found.append(library)


if len(found) == 0:
    raise NoCompatibleLibraries(libraries)
elif len(found) > 1:
    raise MultipleCompatibleLibraries(found)

library = found[0]

if library == "nextcord":
    from nextcord.ext.commands import Bot, AutoShardedBot
    supported_bots = (Bot, AutoShardedBot)

    if TYPE_CHECKING:
        # Duplication is required here because unpack OP in indexes is Python 3.11+ feature.
        # And even with Python 3.11 you'd not be able to dynamically generate Union due to
        # type checkers' static nature. Same applies to other cases as well.
        AnyBot = Union[Bot, AutoShardedBot]

elif library == "disnake":
    from disnake.ext.commands import (
        Bot,
        AutoShardedBot,
        InteractionBot,
        AutoShardedInteractionBot,
    )
    supported_bots = (
        Bot,
        AutoShardedBot,
        InteractionBot,
        AutoShardedInteractionBot,
    )

    if TYPE_CHECKING:
        AnyBot = Union[
            Bot,
            AutoShardedBot,
            InteractionBot,
            AutoShardedInteractionBot,
        ]

else:
    from discord.ext.commands import Bot, AutoShardedBot
    supported_bots = (Bot, AutoShardedBot)

    if TYPE_CHECKING:
        AnyBot = Union[Bot, AutoShardedBot]
