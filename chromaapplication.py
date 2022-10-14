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

    # constructor for application which takes a list of plugins
    def __init__(self, plugins: list = []):

        if plugins:
            # create a list of plugins
            self._plugins = [
                # Import the module and initialise it at the same time
                importlib.import_module(plugin, "./plugins/" + plugin).Plugin() for plugin in plugins
            ]
        else:
            # If no plugin were set we use our default
            self._plugins = [importlib.import_module('default', ".").Plugin()]

    def run(self, stream=stream, recognizer=recognizer):

        print("Starting my application")
        print("-" * 10)
        print("This is my core system")

        for plugin in self._plugins:
            print(plugin)

        print("-" * 10)
        # print("Ending my application")
        print()

        while True:
            if stream.is_active():
                data = stream.read(4096, exception_on_overflow=False)
                if recognizer.AcceptWaveform(data):
                    text = recognizer.Result()
                    print(text[14:-3])
                    stream.stop_stream()
                    for eachPlugin in self._plugins:
                        if eachPlugin.name == text[14:-3].split(" ")[0]:
                            x = threading.Thread(target=eachPlugin.process,
                                                 args=(str((text[14:-3].split(text[14:-3].split(" ")[0])[1])[1:]),),
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
