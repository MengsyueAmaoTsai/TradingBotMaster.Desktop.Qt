
from typing import List
from PySide6.QtGui import QGuiApplication

class DesktopApplication:

    @classmethod
    def create_builder(cls, args: List[str]) -> "DesktopApplicationBuilder":
        """ """
        builder = DesktopApplicationBuilder(args)
    
        return builder
    
class DesktopApplicationBuilder:
    
    def __init__(self, args: List[str]) -> None:
        self.__args = args

    def build(self) -> QGuiApplication:
        app = QGuiApplication()
        return app 