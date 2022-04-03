from cgitb import text
import webbrowser as wb
import time
import keyboard

def whatsapp(number,message):
    num = number
    open_chat = f"https://web.whatsapp.com/send?phone=+91{num}&text={message}" 
    wb.open(open_chat)
    time.sleep(11)
    keyboard.send("enter")

