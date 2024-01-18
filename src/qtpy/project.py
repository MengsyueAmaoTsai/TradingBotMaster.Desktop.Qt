import toml
import os
from pathlib import Path
from typing import Final


class PythonProject:
    """A class to parse the project meta data from the pyproject.toml file."""

    __PROJECT_FILE: Final[str] = "pyproject.toml"

    @classmethod
    def version(cls) -> str:
        """Return the project version."""
        return cls.parse_project_meta().get("version", "")

    @classmethod
    def name(cls) -> str:
        """Return the project name."""
        return cls.parse_project_meta().get("name", "")

    @classmethod
    def parse_project_meta(cls) -> dict[str, str]:
        """Parse the project meta data from the pyproject.toml file."""
        project_path = Path(os.getcwd()) / cls.__PROJECT_FILE

        try:
            with open(project_path, "r", encoding="utf-8") as project:
                return toml.load(project).get("project", {})

        except FileNotFoundError:
            print(f"Error: Could not find the {project_path} file.")
            return {}
