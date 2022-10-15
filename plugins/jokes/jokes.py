import os
import random
import time
import keyboard

import main


class Plugin:

    name = "jokes"
    keywords = ["jokes"]
    author = "neb"
    version = 0.01
    commands = ["spam"]

    spamEnabled = False

    def process(self, text):
        text = text.split(" ", 1)[1]
        print("Plugin running: " + self.name)
        if text not in self.commands:
            print("Invalid command")

        else:
            if text == "spam":
                if self.spamEnabled is False:
                    self.spamEnabled = True
                else:
                    self.spamEnabled = False

                self.spam()

    def spam(self):
        jokes = open("./plugins/jokes/jokes.txt", encoding="utf8")
        jokesList = jokes.readlines()
        while self.spamEnabled:
            randIndex = random.randrange(0, len(jokesList) - 1)
            keyboard.write(jokesList[randIndex].split("<>")[0])
            keyboard.press("Enter")
            time.sleep(2)
            keyboard.write(jokesList[randIndex].split("<>")[1])
            keyboard.press("Enter")
            time.sleep(2)


