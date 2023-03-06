# dispatcher

An extension to easily dispatch custom events for discord bots.

This extension can ideally work with any discord.py fork (disnake, nextcord, pycord) and it comes with typing support for every of these forks.

# Example

```py
import disnake
from disnake import Intents
from disnake.ext import commands

from dispatcher import Dispatcher

bot = commands.Bot(intents=Intents.default(), command_prefix=commands.when_mentioned)
events_dispatcher = Dispatcher(bot, library_name=disnake.__name__) # you can also pass "disnake"

@bot.event
async def on_ready():
    events_dispatcher.dispatch("UwU", 10)

@bot.listen("on_UwU")
async def lmao(x):
    print("UwU", x)
```

```
Out: UwU 10
```

# Installation

- With git
    
    ```
    git clone -b beta https://github.com/Snipy7374/dispatcher --single-branch
    ```
