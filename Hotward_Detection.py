import os
import speech_recognition as sr

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


while True:
    query = TakeCommand()

    if "power off" in query:
        break
    
    elif "power on" in query:
        os.startfile("E:\\Programming\\AI ASSISTANT\\main.py")

    else:
        print("DZ")