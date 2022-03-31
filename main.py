import os
from unittest import result
from winreg import QueryReflectionKey
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
import pywhatkit as py
#import keyboard as kb
import webbrowser
import datetime
import wikipedia
from googletrans import Translator
import requests
import bs4

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

def TakeCommandHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(":) Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(":) Recognizing...")    
        query = r.recognize_google(audio,language="hi")
        print(f":) Your Command : {query}")
    except:
        return "None"
    return query.lower()    

def translate():
    Speak("OK, Tell me the text to translate")
    line = TakeCommandHindi()
    translator = Translator()
    result = translator.translate(line)
    Text = result.text
    Speak(Text)
    while True:
        Speak("Do you wat to translate more sentences ?")
        answer = TakeCommand()
        if answer == "no":
            Speak("OK, closing translator")
            break
        else:
            Speak("OK, Tell me the text to translate")
            line = TakeCommandHindi()
            translator = Translator()
            result = translator.translate(line)
            Text = result.text
            Speak(Text)

def temperature():
    search = "Temperature in pune"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    Speak(f"The temperature is : {temp}")

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
            Speak(f"Opening {query} website")
            webbrowser.open(f"www.{query}.com")

        elif "shutdown computer" in query:
            os.system("shutdown /s /t 0")

        elif "restart computer" in query:
            os.system("shutdown /r /t 0")    
        
        elif "alarm" in query:
            Speak("Please tell me the time to set alarm, for example set alarm at 6:30 am")
            tt = TakeCommand()
            tt = tt.replace("set alarm at ","")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

        elif "start translator" in query:
            translate()
        
        elif "temperature" in query:
            temperature()