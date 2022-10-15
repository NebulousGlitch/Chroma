import os
import _thread
import webbrowser


class Plugin:
    name = "chromautils"
    keywords = ["chromautils", "open", "exit"]
    author = "neb"
    version = 0.01
    commands = []

    listOfMispells = {"spot a thigh": "Spotify", "spot of i": "Spotify", "spot if i": "Spotify",
                      "spot a fire": "Spotify", "bonafide": "Spotify", "spot of fi": "Spotify",
                      "to escort":"discord", "a bolton": "Ableton", "able to":"Ableton", "calculate":"Calculator",
                      "spot i" : "Spotify"}
    webBrowsers = ["chrome", "edge", "microsoft edge", "firefox", "crown"]
    explorerList = {"file explorer", "explorer", "files", "file explore", "file explore rare", "thousand four",
                    "fox four", "fox four" "thoughts for", "packs for", "thanks for", "fire spoiler"}

    def process(self, text):

        if text.split(" ")[0] == "open":
            self.open_program(text)
        if text.split(" ")[0] == "exit":
            self.exit()

    def open_program(self, text):
        newText = text.split(" ", 1)[1]
        if newText == "notepad":
            os.system("notepad.exe")
        elif newText in self.explorerList:
            os.system("explorer.exe")
        elif newText in self.webBrowsers:
            webbrowser.open("google.com")
        else:
            for eachKey in self.listOfMispells.keys():
                if newText == eachKey:
                    newText = self.listOfMispells[eachKey]
            try:
                os.system('start {}:'.format(newText))
            except Exception as e:
                print("Program {} does not exist".format(newText))

    def exit(self):
        _thread.interrupt_main()
