# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Union, List

from pkg_resources import (
    DistributionNotFound,
    get_distribution,
)

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
        AnyBot = Union[*supported_bots]

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
        AnyBot = Union[*supported_bots]

elif library in ("discord", "discord.py"):
    from discord.ext.commands import Bot, AutoShardedBot
    supported_bots = (Bot, AutoShardedBot)

    if TYPE_CHECKING:
        AnyBot = Union[*supported_bots]
