import os
from enum import Enum
from pathlib import Path
from typing import override

from .abstractions import IEnvironment


class Environments(str, Enum):
    """Environments."""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class DesktopEnvironment(IEnvironment):
    """Desktop environment."""

    __slot__ = ("__name", "__content_root_path", "__assets_path")

    DEFAULT_ASSETS_PATH = "assets"
    DEFAULT_SOURCE_PATH = "src"

    def __init__(self, name: str, content_root_path: str, assets_path: str) -> None:
        """Initialize the environment."""
        self.__name = name or Environments.DEVELOPMENT
        self.__content_root_path = Path(content_root_path or os.getcwd())
        self.__assets_path = assets_path or self.DEFAULT_ASSETS_PATH

    @property
    @override
    def content_root_path(self) -> Path:
        """Return the content root path."""
        return self.__content_root_path

    @property
    @override
    def assets_path(self) -> Path:
        """Return the assets path."""
        return self.content_root_path / self.__assets_path

    @property
    @override
    def source_path(self) -> Path:
        """Return the source path."""
        return self.content_root_path / self.DEFAULT_SOURCE_PATH

    @override
    def is_development(self) -> bool:
        """Return True if the environment is development."""
        return self.__name.lower() == Environments.DEVELOPMENT

    @override
    def is_staging(self) -> bool:
        """Return True if the environment is staging."""
        return self.__name.lower() == Environments.STAGING

    @override
    def is_production(self) -> bool:
        """Return True if the environment is production."""
        return self.__name.lower() == Environments.PRODUCTION

    @override
    def __str__(self) -> str:
        return self.__name
