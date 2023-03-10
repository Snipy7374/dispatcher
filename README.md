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

- With pip + Git

    ```
    python3 -m pip install -U git+https://github.com/Snipy7374/dispatcher
    ```

- With Git

    ```
    git clone -b beta https://github.com/Snipy7374/dispatcher --single-branch
    ```

# Development

To contribute, you will need [Git](https://git-scm.com)
and [PDM](https://pdm.fming.dev/). [GitHub CLI](https://cli.github.com/)
will also likely improve your experience.

After installing these, fork this repo and run the
following to setup your development environment:
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_FORK_NAME.git
cd dispatcher
pdm install
pdm run setup_env
```

This will clone the repo, install required dependencies and
setup git hooks ([pre-commit](https://pre-commit.com/), specifically).

After that, the process is common: make changes, commit, push, submit PR.

For big changes it is better to open an issue and discuss your
proposed changes first, to not waste your time in case the change
is undesired.
