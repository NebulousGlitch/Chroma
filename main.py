import os
import sys
import keyboard
from chromaapplication import ChromaApplication


if __name__ == "__main__":
    # getting list of plugins
    plugins = [name for name in os.listdir("./plugins")]

    # adding each plugin to system path
    for eachPlugin in plugins:
        sys.path.append("./plugins/" + eachPlugin)

    app = ChromaApplication(plugins)
    keyboard.add_hotkey("ctrl+space", app.enable_mic)
    # Running our application
    app.run()

