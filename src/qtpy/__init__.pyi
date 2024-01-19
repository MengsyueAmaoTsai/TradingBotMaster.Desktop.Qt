class DesktopApplicationBuilder:
    """DesktopApplicationBuilder class"""

    def build(self) -> DesktopApplication:
        """Build a DesktopApplication instance"""
        ...

class DesktopApplication:
    """DesktopApplication class"""

    @staticmethod
    def create_builder(argv: list[str]) -> DesktopApplicationBuilder:
        """Create a DesktopApplicationBuilder instance"""
        ...

    def run(self) -> None:
        """Run the application"""
        ...
