import sys

import picologging as logging
from env import (
    APP_QML_NAME,
    PROJECT_ROOT_PATH,
    SOURCE_DIR,
    get_project_name,
    get_version,
)
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger()


class DesktopApplication(QGuiApplication):
    def __init__(self, args: list[str]) -> None:
        super().__init__(args)
        version = get_version()
        app_qml_path = PROJECT_ROOT_PATH / SOURCE_DIR / APP_QML_NAME

        # Set application information.
        self.setOrganizationName("Richill Capital")
        self.setOrganizationDomain("richillcapital.com")
        self.setApplicationName(f"<applicationName> {get_project_name()}")
        self.setApplicationDisplayName(f"<applicationDisplayName> {version}")
        self.setApplicationVersion(version)

        # Load the main qml file.
        self.__qml_engine = QQmlApplicationEngine()
        self.__qml_engine.load(app_qml_path)

        # Ensure the application loaded successfully.
        if not self.__qml_engine.rootObjects():
            logger.error("Application failed to load.")
            sys.exit(-1)

    @classmethod
    def create_builder(cls, args: list[str]) -> "DesktopApplicationBuilder":
        return DesktopApplicationBuilder(args)

    def run(self) -> None:
        sys.exit(self.exec())


class DesktopApplicationBuilder:
    def __init__(self, args: list[str]) -> None:
        self.__args = args
        logger.info(f"Args: {args}")

    def build(self) -> DesktopApplication:
        if ("--reload" in self.__args) or ("-r" in self.__args):
            logger.info("Enable hot reload")

        app = DesktopApplication(self.__args)
        return app


app = DesktopApplication.create_builder(sys.argv).build()
app.run()
