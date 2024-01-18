import os
import sys
from pathlib import Path

import picologging
from picologging import DEBUG, Logger, getLogger
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

from .environments import Environments
from .project import PythonProject


class DesktopApplication(QGuiApplication):
    """Desktop application."""

    def __init__(self, args: list[str], content_root_path: Path, assets_path: str) -> None:
        """Initialize the application."""
        super().__init__(args)
        picologging.basicConfig(level=DEBUG, format="%(levelname)s: %(message)s")
        self.__logger = getLogger(DesktopApplication.__name__)

        if ("--reload" in args) or ("-r" in args):
            self.logger.info("Enable hot reload")

        icon_path = content_root_path / assets_path / "logo.jpg"
        icon = QIcon(str(icon_path))
        self.setWindowIcon(icon)

        qml_path = content_root_path / "src" / "App.qml"

        # Load the main qml file.
        self.__qml_engine = QQmlApplicationEngine()
        self.__qml_engine.load(qml_path)

    @property
    def logger(self) -> Logger:
        """Get the logger."""
        return self.__logger

    @classmethod
    def create_builder(
        cls,
        args: list[str],
        app_name: str = "",
        content_root_path: str = "",
        asserts_path: str = "",
        environment_name: str = "",
    ) -> "DesktopApplicationBuilder":
        """Create a builder for the application."""
        return DesktopApplicationBuilder(
            args, app_name, content_root_path, asserts_path, environment_name
        )

    def run(self) -> None:
        """Run the application."""
        if not self.__qml_engine.rootObjects():
            self.logger.error("Application failed to load.")
            sys.exit(-1)

        sys.exit(self.exec())


class DesktopApplicationBuilder:
    """Desktop application builder."""

    def __init__(
        self,
        args: list[str],
        app_name: str,
        content_root_path: str = "",
        assets_path: str = "",
        environment_name: str = "",
    ) -> None:
        """Initialize the builder."""
        self.__args = args
        self.__app_name = app_name
        self.__content_root_path = content_root_path or os.getcwd()
        self.__assets_path = assets_path or "assets"
        self.__environment_name = environment_name or Environments.DEVELOPMENT

    def build(self) -> DesktopApplication:
        """Build the application."""
        app_name = self.__app_name or PythonProject.name()
        version = PythonProject.version()

        QGuiApplication.setOrganizationName("Richill Capital")
        QGuiApplication.setOrganizationDomain("richillcapital.com")
        QGuiApplication.setApplicationName(f"ApplicationName = {app_name} - {version}")
        QGuiApplication.setApplicationDisplayName(
            f"ApplicationDisplayName = {app_name} - {version}"
        )
        QGuiApplication.setApplicationVersion(version)

        app = DesktopApplication(
            self.__args,
            content_root_path=Path(self.__content_root_path),
            assets_path=self.__assets_path,
        )

        return app


__all__ = ["DesktopApplication", "DesktopApplicationBuilder"]
