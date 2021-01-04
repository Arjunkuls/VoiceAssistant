import time
import os
from gtts import gTTS
import playsound
from speak import speak
import subprocess
import datetime
from googlesearch import search
import webbrowser

def makenote(text):
    date = datetime.datetime.now()
    filename = str(date).replace(':', "_") + '_note.txt'
    with open(filename, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", filename])

def thetime():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days = ["Monday", "Tuesday", "Wednusday", "Thursday", "Friday", "Saturday", "Sunday"]
    x = time.localtime()
    year = x.tm_year
    monthkey=x.tm_mon - 1
    daykey = x.tm_wday
    minutes = str(x.tm_min)
    hours = int(x.tm_hour)
    if hours > 12:
        hours=hours-12
    day = days[daykey]
    month = months[monthkey]
    speak(f'It is {minutes} minutes past {hours} oclock on {day} in the month of {month} in the year {year}')


def research(query):
    q = search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=1)
    webbrowser.open(q, new=2)