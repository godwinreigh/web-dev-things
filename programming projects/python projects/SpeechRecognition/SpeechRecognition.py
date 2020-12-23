import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser


not_done = True
while not_done:
    r = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone(1) as source:
        engine.say("Speak Now")
        print("Speak Now: ")
        r.energy_threshold = 17000
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
                not_done = False


        except:
            print("Invalid, please try again")
            engine.say("Invalid please try again")
            pass
exit()
quit()