from takeinput import listenup
import time
import os
from gtts import gTTS
import playsound
from speak import speak
import subprocess
import datetime
from commmands import *
import sys
from googlesearch import search

running = True
while running:
    speak("GIve your command")
    textup = listenup()
    text = textup.lower()

    if "note" in text:
        speak("What sould be in the note")
        content = listenup()
        makenote(content)

    elif "time" in text or "date" in text:
        thetime()

    elif "end" in text or "by" in text or "quit" in text:
        speak("Shutting Down")
        sys.exit()

    elif "greet" in text or "hello" in text:
        speak("Hello, I am a Python Voice Assistant")

    elif "google" in text:
        speak("What would you like me to google")
        query = listenup()
        research()

    else:
        speak("Command not recognised")