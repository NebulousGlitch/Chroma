import pyttsx3


def speak(text, speed_value=None):
    engine = pyttsx3.init()
    if speed_value is None:
        engine.say(text)
        engine.runAndWait()
    else:
        engine.setProperty("speed", speed_value)
        engine.say(text)
        engine.runAndWait()
