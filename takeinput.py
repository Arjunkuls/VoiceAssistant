import speech_recognition as sr

r = sr.Recognizer()

def listenup():
    with sr.Microphone() as src:
        audio = r.listen(src)
        try:
            text = r.recognize_google(audio)
            print(text)

        except:
            text = "Recognition failure"

    return text