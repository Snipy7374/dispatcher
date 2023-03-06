import os
import logging
import shutil

from jinja2 import Environment, FileSystemLoader

_log = logging.getLogger(__name__)


class Generator:
    def __init__(self, library: str) -> None:
        self.environment = Environment(
            loader=FileSystemLoader("ext_dispatcher/generator/templates"),
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
        if files := os.scandir(path="ext_dispatcher/types"):
            for file in files:
                # if exists file types of other libraries delete them
                if not file.name.startswith(self.library_name):
                    if file.is_file():
                        _log.debug("found an old file types (%s), removing it", file.name)
                        os.remove(f"ext_dispatcher/types/{file.name}")
                    else:
                        shutil.rmtree(f"ext_dispatcher/types/{file.name}")
                
                # if file types for the user provided library already exists skip this process
                if file.name.startswith(self.library_name):
                    _log.info("%s types already exists, skipping this process", self.library_name)
                    return
 
        content = self._render_template("types.py.jinja")
        with open(f"ext_dispatcher/types/{self.library_name}_types.py", "w") as file:
            file.write(content)
        _log.debug("created file types for %s at %s", self.library_name, file.name)

        init_content = self._render_template("__init__.py.jinja")
        with open("ext_dispatcher/types/__init__.py", "w") as file:
            file.write(init_content)
        _log.debug("created init file for %s at %s", self.library_name, file.name)
        _log.info("file types created")