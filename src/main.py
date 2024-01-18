from qtpy import DesktopApplication
import sys

app = DesktopApplication.create_builder(sys.argv).build()
app.run()
