import urllib
import webbrowser

class Plugin:

    name = "search"
    author = "neb"
    version = 0.01
    commands = ["google", "tube", "wikipedia"]

    def process(self, text):
        print("Plugin running: " + self.name)
        if text.split(" ")[-1] not in self.commands:
            self.search(text)
        else:
            if text.split(" ")[-1] == "tube":
                self.search_on_youtube(text.split(" ")[1:])
            print("searching on youtube")

    def search(self, query):
        if query == "never gonna give you up":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0,
                            autoraise=True)
        else:
            webbrowser.open("https://www.google.com/search?q=`" + urllib.parse.quote_plus(query), new=0, autoraise=True)

    def search_on_youtube(self, query):
        if query == "never gonna give you up on youtube":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0,
                            autoraise=True)
        else:
            webbrowser.open("https://www.youtube.com/results?search_query=" + (urllib.parse.quote_plus(query)).split(" on you tube")[0], new=0, autoraise=True)

