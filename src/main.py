import sys

from qtpy import DesktopApplication

if __name__ == "__main__":
    builder = DesktopApplication.create_builder(sys.argv)

    app = builder.build()

    app.run()
