from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias

from disnake import Client, AutoShardedClient
from disnake.ext.commands import Bot, AutoShardedBot

from disnake.ext.commands import InteractionBot, AutoShardedInteractionBot

AnyBot: TypeAlias = Union[
    Client,
    AutoShardedClient,
    Bot,
    AutoShardedBot,
    InteractionBot,
    AutoShardedInteractionBot,
]