"""
MIT License

Copyright (c) 2023 Snipy7374

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import logging
import shutil

from jinja2 import Environment, FileSystemLoader

_log = logging.getLogger(__name__)
BASE_DIR = "dispatcher/"
TYPES_DIR = BASE_DIR + "types/"

class Generator:
    def __init__(self, library: str) -> None:
        self.environment = Environment(
            loader=FileSystemLoader(BASE_DIR + "generator/templates"),
            lstrip_blocks=True,
            trim_blocks=True,
        )
        self.library_name = library
    
    def _render_template(self, template_name: str) -> str:
        """An internal method used to generate templates."""
        template = self.environment.get_template(template_name)
        return template.render(library=self.library_name)

    def _generate_types(self):
        """This method handles the logic of file types creation."""
        _log.info("generating file types for %s", self.library_name)
        if files := os.scandir(path=TYPES_DIR):
            for file in files:
                # if exists file types of other libraries delete them
                if not file.name.startswith(self.library_name):
                    if file.is_file():
                        _log.debug("found an old file types (%s), removing it", file.name)
                        os.remove(TYPES_DIR + file.name)
                    else:
                        shutil.rmtree(TYPES_DIR + file.name)
                
                # if file types for the user provided library already exists skip this process
                if file.name.startswith(self.library_name):
                    _log.info("%s types already exists, skipping this process", self.library_name)
                    return
 
        content = self._render_template("types.py.jinja")
        with open(f"{TYPES_DIR}{self.library_name}_types.py", "w") as file:
            file.write(content)
        _log.debug("created file types for %s at %s", self.library_name, file.name)

        init_content = self._render_template("__init__.py.jinja")
        with open(TYPES_DIR + "__init__.py", "w") as file:
            file.write(init_content)
        _log.debug("created init file for %s at %s", self.library_name, file.name)
        _log.info("file types created")