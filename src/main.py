import sys

from qtpy import DesktopApplication

if __name__ == "__main__":
    app = DesktopApplication.create_builder(sys.argv, environment="Production").build()

    if app.environment.is_development():
        print("Development mode is enabled.")
    elif app.environment.is_production():
        print("Production mode is enabled.")
    elif app.environment.is_staging():
        print("Staging mode is enabled.")

    print(app.environment)
    app.run()
