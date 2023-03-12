# This example uses disnake

from disnake.ext import commands
from dispatcher import Dispatcher

class MyBot(commands.Bot):
    dispatcher: Dispatcher["MyBot"]

    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=None,
        )
        self.dispatcher = Dispatcher(self)

    async def on_ready(self):
        print(self.user)
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