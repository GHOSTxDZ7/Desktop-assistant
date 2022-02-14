import os
import pyttsx3
import speech_recognition as sr
import pywhatkit as py
#import keyboard as kb
import webbrowser
import datetime
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",187)

def Speak(audio):
    print("   ")
    print(f":) {audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()
'''
def autoYT():
    while True:
        query = TakeCommand()
        if "exit" in query:
            Speak("autoYT has stopped") 
        elif "pause" or "resume" in query:
            kb.press("space bar")
        elif "full screen" in query:
            kb.press("f")
        elif "default view" in query:
            kb.press("t")
        elif "miniplayer mode" in query:
            kb.press("i")
        elif "next video" in query:
            kb.press_and_release("shift + n")
        elif "previous video" in query:
            kb.press_and_release("shift + p")
        elif "increase speed" in query:
            kb.press_and_release("shift + .")
        elif "decrease speed" in query:
            kb.press_and_release("shift + ,")
        elif "fast forward" in query:
            kb.press("l")
        elif "rewind" in query:
            kb.press("j")
        elif "mute" or "umute" in query:
            kb.press("m")
 '''

    
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(":) Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(":) Recognizing...")    
        query = r.recognize_google(audio,language="en-in")
        print(f":) Your Command : {query}")
    except:
        return "None"
    return query.lower()    

if __name__=="__main__":
    Speak("Hello, how may I help you. ")
    while True:
        query = TakeCommand()

        if "exit" in query:
            Speak("OK, you can call me anytime.")
            break
        elif "play" and "on youtube" in query:
            query = query.replace("play","")
            query = query.replace("on youtube","")
            Speak("ok just a second")
            py.playonyt(query)
        elif "google search" in query:
            Speak("Ok, This is what I have found on Google")
            query = query.replace("google search","")
            py.search(query)
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"The time is {strTime}")   
            Speak(f"The time is {strTime}")
        elif "wikipedia" in query:
            Speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Speak("According to Wikipedia")
            Speak(results)
        elif "open" and "website" in query:
            query = query.replace("open ","")
            query = query.replace(" website","")
            webbrowser.open(f"www.{query}.com")
        

             

   