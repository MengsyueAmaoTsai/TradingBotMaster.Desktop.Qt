from pathlib import Path

import toml

PROJECT_ROOT_PATH = Path(__file__).parent.parent
PROJECT_FILE = "pyproject.toml"

SOURCE_DIR = "src"

APP_QML_NAME = "App.qml"


# TOML parsing
def get_version() -> str:
    version = ""
    try:
        with open(PROJECT_FILE, "r", encoding="utf-8") as project:
            data = toml.load(project)
            version = data["project"]["version"]

            return version

    except FileNotFoundError:
        print(f"Error: Could not find the {PROJECT_FILE} file.")
        return version

    except KeyError:
        print("Error: Unable to find the correct fields for version.")
        return version


def get_project_name() -> str:
    name = ""

    try:
        with open(PROJECT_FILE, "r", encoding="utf-8") as project:
            data = toml.load(project)
            name = data["project"]["name"]

            return name

    except FileNotFoundError:
        print(f"Error: Could not find the {PROJECT_FILE} file.")
        return name

    except KeyError:
        print("Error: Unable to find the correct fields for application name.")
        return name
