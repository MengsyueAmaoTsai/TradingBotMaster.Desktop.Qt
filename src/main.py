import gc
import sys

from qtpy import DesktopApplication
from view_models import MainViewModel

if __name__ == "__main__":
    gc.set_debug(gc.DEBUG_STATS)

    builder = DesktopApplication.create_builder(sys.argv)

    view_model = MainViewModel()

    app = builder.build()
    app.run()
