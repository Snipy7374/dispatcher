# SPDX-License-Identifier: MIT

# This example uses disnake

import disnake
from disnake.ext import commands

from dispatcher import Dispatcher

bot = commands.Bot(command_prefix=commands.when_mentioned, intents=None)
bot.dispatcher = Dispatcher(bot, library_name=disnake.__name__)


@bot.event
async def on_ready():
    print(bot.user)
    bot.dispatcher.dispatch("my_event")

    # passing args and kwargs
    bot.dispatcher.dispatch("my_second_event", 10, name="Snipy")


@bot.listen("on_my_event")
async def foo():
    print("on_my_event was called")


@bot.listen("on_my_second_event")
async def bar(n, *, name):
    print("on_my_second_event was called", n, name)


bot.run("TOKEN")
