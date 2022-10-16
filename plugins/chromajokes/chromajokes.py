import random
import time
import keyboard

import tts


class Plugin:

    name = "chromajokes"
    keywords = {"jokes":True, "tell me a joke":True}
    author = "neb"
    version = 0.01
    commands = ["spam"]

    spamEnabled = False

    def process(self, text):
        print("Plugin running: " + self.name)
        if text not in self.keywords:
            print("Invalid command")

        else:
            if text == "spam":
                if self.spamEnabled is False:
                    self.spamEnabled = True
                else:
                    self.spamEnabled = False

                self.spam()
            if text == "tell me a joke":
                self.tell_me_a_joke()

    def spam(self):
        jokes = open("./plugins/chromajokes/jokes.txt", encoding="utf8")
        jokesList = jokes.readlines()
        while self.spamEnabled:
            randIndex = random.randrange(0, len(jokesList) - 1)
            keyboard.write(jokesList[randIndex].split("<>")[0])
            keyboard.press("Enter")
            time.sleep(2)
            keyboard.write(jokesList[randIndex].split("<>")[1])
            keyboard.press("Enter")
            time.sleep(2)

    def tell_me_a_joke(self):
        jokesList = ""
        print("Running tell me a joke")
        with open("./plugins/chromajokes/jokes.txt", encoding="utf8") as j:
            jokesList = j.readlines()
        randIndex = random.randrange(0, len(jokesList) - 1)
        tts.speak(jokesList[randIndex].split("<>")[0])
        time.sleep(1)
        tts.speak(jokesList[randIndex].split("<>")[1])

