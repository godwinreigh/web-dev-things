import speech_recognition as sr
import pyttsx3
import webbrowser
import pyaudio
from tkinter import *
root = Tk()

def voice():
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    engine = pyttsx3.init()

    with sr.Microphone(1) as source:
        engine.say("Speak Now")
        print("Speak Now: ")
        r.energy_threshold = 28000
        engine.runAndWait()
        audio = r.listen(source)

        try:
            text = str(r.recognize_google(audio,language='en-PH')).lower()
            print(text)

            if text == 'hey google':
                webbrowser.open("www.google.com")
                engine.say("Google is opened")
            elif text == 'open facebook':
                webbrowser.open('www.facebook.com')
                engine.say("Facebook is opened")
            elif text == 'exit':
                engine.say("Goodbye")
                print("Goodbye")
                pass


        except:
            print("Invalid, please try again")
            engine.say("Invalid please try again")
            voice()
mylabel = Label(root,text="Speech recognition")
mylabel.pack()
mybtn1= Button(root, text="SPEAK NOW", command=voice)
mybtn1.pack()
mainloop()