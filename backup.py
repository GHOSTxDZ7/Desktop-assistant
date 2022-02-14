import os
import pyttsx3
import speech_recognition as sr
import pywhatkit as py
import keyboard as kb
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',187)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(":) Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f":) User said: {query}\n")

    except Exception as e:
        # print(e)    
        print(":) Please say that again ...")  
        return "None"
    return query

if __name__=="__main__":
    while True:
        query = takeCommand().lower()

        if 'exit' in query:
            speak('OK, you can call me anytime.')
            break
        elif 'hello' in query:
            speak('Hello, how may I help you. ')
        elif 'play' and 'on youtube' in query:
            query = query.replace('play','')
            query = query.replace('on youtube','')
            speak('ok just a second')
            py.playonyt(query)
        elif 'google search' in query:
            speak('Ok, This is what I have found on Google')
            query = query.replace('google search','')
            py.search(query)
        elif 'open' and 'website' in query:
            query = query.replace('open','')
            query = query.replace('website','')
            website = 'https://www.'+ query + '.com'
            speak(f'Opening...{query} website')
            webbrowser.open(website)