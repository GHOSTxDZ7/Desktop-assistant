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
            kb.press('spacebar')
        elif 'full screen' in query:
            kb.press('f')
        elif 'default view' in query:
            kb.press('t')
        elif 'miniplayer mode' in query:
            kb.press('i')
        elif 'next video' in query:
            kb.press_and_release('shift + n')
        elif 'previous video' in query:
            kb.press_and_release('shift + p')
        elif 'increase speed' in query:
            kb.press_and_release('shift + .')
        elif 'decrease speed' in query:
            kb.press_and_release('shift + ,')
        elif 'fast forward' in query:
            kb.press('l')
        elif 'rewind' in query:
            kb.press('j')
        elif 'mute' or 'umute' in query:
            kb.press('m')
YT()                 