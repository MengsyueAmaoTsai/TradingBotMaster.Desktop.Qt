from enum import Enum


class Environments(str, Enum):
    """Environments."""

    DEVELOPMENT = "development"
    PRODUCTION = "production"
