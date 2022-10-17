import os
import sys
import threading
import keyboard

from chromaapplication import ChromaApplication
from gui import GUI

if __name__ == "__main__":
    # getting list of plugins
    plugins = [name for name in os.listdir("./plugins")]

    # adding each plugin to system path
    for eachPlugin in plugins:
        sys.path.append("./plugins/" + eachPlugin)

    app = ChromaApplication(plugins)
    keyboard.add_hotkey("ctrl+space", app.enable_mic)
    threading.Thread(target=app.run, daemon=True).start()
    gui = GUI()
    gui.initialize()







