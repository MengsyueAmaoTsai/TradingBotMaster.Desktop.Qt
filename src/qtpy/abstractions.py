from pathlib import Path
from typing import Protocol, override


class IEnvironment(Protocol):
    """Environment interface."""

    @property
    def content_root_path(self) -> Path:
        """Return the content root path."""
        ...

    @property
    def assets_path(self) -> Path:
        """Return the assets path."""
        ...

    @property
    def source_path(self) -> Path:
        """Return the source path."""
        ...

    def is_development(self) -> bool:
        """Return True if the environment is development."""
        ...

    def is_staging(self) -> bool:
        """Return True if the environment is staging."""
        ...

    def is_production(self) -> bool:
        """Return True if the environment is production."""
        ...

    @override
    def __str__(self) -> str:
        ...
