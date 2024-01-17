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


class DesktopApplication:
    def __init__(self) -> None:
        # Initialize Qt Gui app
        app_name = get_project_name()
        version = get_version()
        app_qml_path = PROJECT_ROOT_PATH / SOURCE_DIR / APP_QML_NAME

        self.__qt_app = QGuiApplication()
        self.__qt_app.setOrganizationName("Richill Capital")
        self.__qt_app.setOrganizationDomain("richillcapital.com")
        self.__qt_app.setApplicationName(f"<applicationName> {app_name}")
        self.__qt_app.setApplicationDisplayName(f"<applicationDisplayName> {version}")
        # app.setWindowIcon()

        # Initialize QML Engine
        self.__qml_engine = QQmlApplicationEngine()
        self.__qml_engine.load(app_qml_path)

    @classmethod
    def create_builder(cls, args: list[str]) -> "DesktopApplicationBuilder":
        return DesktopApplicationBuilder(args)

    def run(self) -> None:
        if not self.__qml_engine.rootObjects():
            logger.error("No any object in qml engine.")
            sys.exit(-1)

        sys.exit(self.__qt_app.exec())


class DesktopApplicationBuilder:
    def __init__(self, args: list[str]) -> None:
        self.__args = args

        logger.info(f"Args: {args}")

    def build(self) -> DesktopApplication:
        if ("--reload" in self.__args) or ("-r" in self.__args):
            logger.info("Enable hot reload")

        app = DesktopApplication()
        return app


builder = DesktopApplication.create_builder(sys.argv)
app = builder.build()
app.run()
