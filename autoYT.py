import keyboard as kb
from pip import main
import pyttsx3
import speech_recognition as sr
import main

def YT():
    while True:
        query = main.TakeCommand().lower()
        if 'exit' in query:
            main.Speak('autoYT has stopped')
            break 
        elif 'pause' or 'resume' in query:
            kb.send('spacebar')
        elif 'full screen' in query:
            kb.send('f')
        elif 'default view' in query:
            kb.send('t')
        elif 'miniplayer mode' in query:
            kb.send('i')
        elif 'next video' in query:
            kb.send('shift + n')
        elif 'previous video' in query:
            kb.send('shift + p')
        elif 'increase speed' in query:
            kb.send('shift + .')
        elif 'decrease speed' in query:
            kb.send('shift + ,')
        elif 'fast forward' in query:
            kb.send('l')
        elif 'rewind' in query:
            kb.send('j')
        elif 'mute' or 'umute' in query:
            kb.send('m')
YT()                 