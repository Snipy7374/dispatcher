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

        # Send message to any available channel.
        for guild in self.guilds:
            for channel in guild.text_channels:
                await channel.send("Hello!")
                break
            break

    async def on_message(self, message: disnake.Message) -> None:
        # The message is sent by us.
        if message.author.id == self.user.id:
            # Dispatch the 'on_self_message' event.
            self.dispatcher.dispatch("on_self_message", message)

    # Event listeners can be defined on bot class itself..
    async def on_self_message(self, message: disnake.Message):
        print(f"Self-sent message at {message.created_at}")


bot = MyBot()


# ..or be registered as a listener, either via @commands.Bot.listen or
# @commands.Cog.listener() decorators..
@bot.listen("on_self_message")
async def log_content(message: disnake.Message) -> None:
    print(f"Self-sent message with content '{message.content}'")


# ..just like the regular events.
try:
    bot.run(os.environ["BOT_TOKEN"])
except KeyError:
    print("Unable to find bot token. Have you set the 'BOT_TOKEN' environment variable?")
    exit(1)
