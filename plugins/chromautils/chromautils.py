import os
import _thread
import webbrowser
import chromaapplication
from pydictionary import Dictionary

import tts


class Plugin:
    name = "chromautils"
    keywords = {"chromautils":True, "open":True, "exit":True, "dictate":True, "opening":True, "definition of":False, "define":True}
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
        text = text.lower()
        if text.split(" ")[0] == "open" or text.split(" ")[0] == "opening":
            self.open_program(text)
        if text.split(" ")[0] == "exit":
            self.exit()
        if text.split(" ")[0] == "dictate":
            self.dictate()
        if "definition of" in text or "define" in text.split(" ")[0]:
            if "definition of" in text:
                print(text.split("definition of ")[1])
                self.define((text.split("definition of ")[1]))

            else:
                print("".join((text.split("define ")[1])))
                self.define("".join((text.split("define ")[1])))

    def define(self, word):
        definition = Dictionary(word, 1)
        print(definition.meanings())
        tts.speak(definition.meanings())

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

    def dictate(self):
        chromaapplication.dictate = True