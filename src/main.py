import sys

from qtpy import DesktopApplication

if __name__ == "__main__":
    app = DesktopApplication.create_builder(sys.argv).build()
    app.run()
