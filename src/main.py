import sys

from qtpy import DesktopApplication
from view_models import MainViewModel

if __name__ == "__main__":
    builder = DesktopApplication.create_builder(sys.argv)

    view_model = MainViewModel()

    app = builder.build()
    app.run()
