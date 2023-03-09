import re
from setuptools import setup

version = ""
with open("dispatcher/__init__.py", encoding="utf-8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

setup(
    version=version,
    packages=["dispatcher"],
)
