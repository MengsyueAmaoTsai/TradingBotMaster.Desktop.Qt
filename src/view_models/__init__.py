from PySide6.QtCore import QObject


class MainViewModel(QObject):
    """Main view model."""

    def __init__(self) -> None:
        """Initialize the view model."""
        super().__init__()


__all__ = ["MainViewModel"]
