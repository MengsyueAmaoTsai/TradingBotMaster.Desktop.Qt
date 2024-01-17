from pathlib import Path

import toml
import os

PROJECT_ROOT_PATH = Path(os.path.abspath(os.getcwd()))
PROJECT_FILE = "pyproject.toml"

SOURCE_DIR = "src"

APP_QML_NAME = "App.qml"


def get_version() -> str:
    version = parse_project_meta().get("version", "")

    if not version:
        print("Error: Unable to find the correct fields for version.")

    return version


def get_project_name() -> str:
    project_name = parse_project_meta().get("name", "")

    if not project_name:
        print("Error: Unable to find the correct fields for application name.")

    return project_name


def parse_project_meta() -> dict[str, str]:
    try:
        with open(PROJECT_FILE, "r", encoding="utf-8") as project:
            return toml.load(project).get("project", {})

    except FileNotFoundError:
        print(f"Error: Could not find the {PROJECT_FILE} file.")
        return {}
