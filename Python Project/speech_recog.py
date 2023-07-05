import speech_recognition as sr

import pyttsx3 as p

r1 = sr.Recognizer()

engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello Sir, How are you today")
engine.runAndWait()


    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source)

        audio = r1.listen(source)

        try:
            text = r1.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            print("Unknown value")
        except sr.RequestError as e:
            print("Request error")