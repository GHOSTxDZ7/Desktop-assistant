import datetime
from lib2to3.pgen2.token import MINUS
import winsound
import main

def alarm(timing):
    time = str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    time = time[11:-3]
    hours = time[:2]
    hours = int(hours)
    minutes = time[3:5]
    minutes = int(minutes)
    
    main.Speak(f"Done, alarm is set for {timing}")

    while True:
        if hours == datetime.datetime.now().hour:
            if minutes == datetime.datetime.now().minute:
                print("wake-up")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif minutes<datetime.datetime.now().minute:
                break

