# SPDX-License-Identifier: MIT

# Basic functionality example using disnake.

import os

import disnake
from disnake.ext import commands

from dispatcher import Dispatcher


# We don't need prefix commands, so we are using InteractionBot here.
class MyBot(commands.InteractionBot):
    # Dispatcher uses generics so that you can use any bot
    # class from any library: you just need to type-hint it.
    dispatcher: Dispatcher["MyBot"]

    def __init__(self) -> None:
        super().__init__(intents=disnake.Intents.default())
        # One would usually assign dispatcher to the bot directly.
        self.dispatcher = Dispatcher(self)

    async def on_ready(self) -> None:
        print(f"Ready! Logged in as {self.user}")

    async def on_message(self, message: disnake.Message) -> None:
        # We're mentioned in the message.
        if self.user.id in [user.id for user in message.mentions]:
            # Dispatch the 'on_self_message' event.
            self.dispatcher.dispatch("on_self_mention", message)

    # Event listeners can be defined on bot class itself..
    async def on_self_mention(self, message: disnake.Message):
        print(f"We were mentioned at {message.created_at}")


bot = MyBot()


# ..or be registered as a listener, either via @commands.Bot.listen or
# @commands.Cog.listener() decorators, just like the regular events.
@bot.listen("on_self_mention")
async def log_author(message: disnake.Message) -> None:
    print(f"We were mentioned in message sent by '{message.author}'")


try:
    bot.run(os.environ["BOT_TOKEN"])
except KeyError:
    print("Unable to find bot token. Have you set the 'BOT_TOKEN' environment variable?")
    exit(1)
