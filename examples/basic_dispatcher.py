# SPDX-License-Identifier: MIT

# Basic functionality example using disnake.

from disnake.ext import commands

from dispatcher import Dispatcher

class MyBot(commands.InteractionBot):
    dispatcher: Dispatcher["MyBot"] # Dispatcher uses generics so that you can use any bot
                                    # class from any library: you just need to type-hint it.

    def __init__(self) -> None:
        super().__init__(intents=None)
        self.dispatcher = Dispatcher(self)

    async def on_ready(self):
        print(f"Ready! Logged in as {self.user}")
        self.dispatcher.dispatch("my_event")

        # passing args and kwargs
        self.dispatcher.dispatch("my_second_event", 10, name="Snipy")

bot = MyBot()


@bot.listen("on_my_event")
async def foo():
    print("on_my_event was called")


@bot.listen("on_my_second_event")
async def bar(num: int, *, name: str):
    print("on_my_second_event was called", num, name)


bot.run("TOKEN")
