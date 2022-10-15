# Chroma
A simple yet versatile voice assistant coded in Python

*This project is based around Vosk's small model for speech recognition.* 

There aren't many practical voice assistants that are completely local. Furthermore, the goal of this project is to make a consistent, helpful voice recognition program to speed up workflows. 
To use the voice assistant, the current keybind is Control + Space. When the keybind is pressed, the mic stream will open, allowing the data to be read into the recognizer. Thus, the program is NOT constantly listening for keyword, like "Hello Chroma." 

This program is meant to be plugin-based, so the functionality of the program can be expanded well beyond the default plugins. 

Goals:
- Work on a the basic functionality (default plugins)
- Optimize the code and improve recognition without changing the model (important, as the model is very innacurate when it comes to common programs)
- Eventually, make a small gui or indicator showing when the voice assistant is on 

