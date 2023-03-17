<!-- SPDX-License-Identifier: MIT -->

# disnake-ext-dispatcher

An extension to easily dispatch custom events for discord bots.

This extension can ideally work with any discord.py-derived library (e.g., disnake, nextcord, pycord) and
comes with full typing support for every of them.

## Installation

Currently there isn't package available on PyPI, so you'll have to install this with Git:

```sh
python3 -m pip install -U git+https://github.com/Snipy7374/dispatcher
```

## Examples

See the [examples](/examples) folder.

## Development

To contribute, you will need [Git](https://git-scm.com)
and [PDM](https://pdm.fming.dev/). [GitHub CLI](https://cli.github.com/)
will also likely improve your experience.

After installing these, fork this repo and run the
following to setup your development environment:

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_FORK_NAME.git
cd dispatcher
pdm install -d -G lint
pdm run setup_env
```

This will clone the repo, install required dependencies and
setup git hooks ([pre-commit](https://pre-commit.com/), specifically).

After that, the process is common: make changes, commit, push, submit PR.

For big changes it is better to open an issue and discuss your
proposed changes first, to not waste your time in case the change
is undesired.
