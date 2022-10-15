import importlib
import threading
from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16
from playsound import playsound


class ChromaApplication:
    model = Model("./models/vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)

    mic = PyAudio()
    stream = mic.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.stop_stream()

    possibleKeywords = set()

    # constructor for application which takes a list of plugins
    def __init__(self, plugins: list = []):

        if plugins:
            # create a list of plugins
            self._plugins = [
                importlib.import_module(plugin, "./plugins/" + plugin).Plugin() for plugin in plugins
            ]

            #generate a set of keywords for quick search
            for eachPlugin in self._plugins:
                for eachKeyword in eachPlugin.keywords:
                    if eachKeyword not in self.possibleKeywords:
                        self.possibleKeywords.add(eachKeyword)

    def run(self, stream=stream, recognizer=recognizer):

        print("Starting my application")
        print("-" * 10)
        print("Running with the following plugins:")

        for plugin in self._plugins:
            print(plugin)

        print("-" * 10)
        # print("Ending my application")
        print()

        while True:
            if stream.is_active():
                data = stream.read(4096, exception_on_overflow=False)
                if recognizer.AcceptWaveform(data):
                    stream.stop_stream()
                    text = recognizer.Result()[14:-3]
                    print(text)

                    if text.split(" ")[0] in self.possibleKeywords:
                        x = threading.Thread(target=next(x for x in self._plugins if text.split(" ")[0] in x.keywords).process,
                                             args=(text,),
                                             daemon=True)
                        x.start()

                    playsound("./assets/sfx/voiceoff.mp3", False)

    def enable_mic(self):

        if self.stream.is_stopped():
            self.stream.start_stream()
            playsound("./assets/sfx/voiceon.mp3", False)

        else:
            self.stream.stop_stream()
            playsound("./assets/sfx/voiceoff.mp3", False)
