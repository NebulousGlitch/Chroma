import urllib
import webbrowser


class Plugin:
    name = "chromasearch"
    keywords = {"search": True}
    author = "neb"
    version = 0.01
    commands = []

    def process(self, text):
        print("Plugin running: " + self.name)
        if text.split(" ")[-1] not in self.commands:
            self.search("".join(text.split(" ", 1)[1:]))
        else:
            if text.split(" ")[-1].lower() == "youtube":
                self.search_on_youtube("".join(text.split(" ", 1)[1:]))
            print("searching on youtube")

    def search(self, query):
        if query == "never gonna give you up":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0,
                            autoraise=True)
        else:
            webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote_plus(query), new=0, autoraise=True)

    def search_on_youtube(self, query):
        if query == "never gonna give you up on youtube":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0,
                            autoraise=True)
        else:
            webbrowser.open("https://www.youtube.com/results?search_query=" + (
                urllib.parse.quote_plus(query.split(" on youtube")[0])), new=0, autoraise=True)

    def search_on_wikipedia(self, query):
        webbrowser.open("https://en.wikipedia.org/wiki/" + query.replace(" ", "_"))
