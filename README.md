# Chroma
A simple yet versatile voice assistant coded in Python

*This project is based around Vosk's small model for speech recognition.* 

There aren't many practical voice assistants that are completely local. Furthermore, the goal of this project is to make a consistent, helpful voice recognition program to speed up workflows. 
To use the voice assistant, the current keybind is Control + Space. When the keybind is pressed, the mic stream will open, allowing the data to be read into the recognizer. Thus, the program is NOT constantly listening for keyword, like "Hello Chroma." 

This program is meant to be plugin-based, so the functionality of the program can be expanded well beyond the default plugins. An example of how one could use the program is by simply saying "open [program name]." One could also use the program by saying something like "search [text] on youtube." 

### Goals:
- Work on a the basic functionality (default plugins)
  - basic functionality includes opening programs, defining words, searching stuff, etc. 
- Optimize the code and improve recognition without changing the model (important, as the model is very innacurate when it comes to common programs and names)
- Code speech recognition in C to speed up the program 
- Eventually, make a small gui or indicator showing when the voice assistant is on 
- Possibly add a chat bot feature, if an efficient model ever releases 
