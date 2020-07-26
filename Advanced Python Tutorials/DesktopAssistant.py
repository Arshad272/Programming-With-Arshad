import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import os
import pyautogui
from tkinter import *

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
volume = engine.getProperty('rate')
engine.setProperty('rate',130)
def speak(text):
    engine.say(text)
    engine.runAndWait()

hour = int(time.strftime("%H"))

if hour >= 0 and hour < 12:
    wish = "Good Morning"

elif hour >= 12 and hour < 16 :
    wish = "Good Afternoon"

else:
    wish = "Good Evening"


def start_up():
    print(wish+" Arshad")
    speak(wish+" Arshad")
    print("Iam Your Personal Assistant")
    speak("Iam Your Personal Assistant")
    print("Please Click on help")
    speak("Please Click on help")

start_up()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" -- Iam Listening --")
        speak("Iam Listening")
        audio = r.listen(source)
    
    try:
        print(" -- Iam Recognizing --")
        speech = r.recognize_google(audio)
        print(f" Your Speech Is : {speech}")
        speech = speech.lower()
        return speech
        
    
    except:
        print("Iam Unable to recognise")

def action():
    my_query = take_command()

    if 'open whatsapp' in my_query:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://web.whatsapp.com/")
        speak("opening whatsapp")
        
    elif 'open facebook' in my_query:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.facebook.com/")
        speak("openong facebook")

    elif 'open camera' in my_query:
        os.startfile("microsoft.windows.camera:")
        speak("opening camera")

    elif 'open control panel' in my_query:
        os.system("control panel")
        speak("Opening control panel")

    elif 'open my website' in my_query:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://arshad272.github.io/home")
        speak("Opening your persoanl website")

    elif 'open' or 'what' or 'why' or 'how' in my_query:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.com/")
        time.sleep(3)
        pyautogui.write(my_query, interval = 0.05)
        pyautogui.press('enter')
        speak("I found this")

    else:
        print("Iam Unable to recognise")
        speak("Iam unable to recognise")

window = Tk()

window.title("Desktop Assistant")
label = Label(window, text= "Hello Arshad\nIam Your Personal Assistant\nPlease Click on Help",bg="black", fg = 'white', font=("Times New Roman",25))
label.pack()
btn = Button(window, text= "Help", bg = 'blue',font=("Times New Roman",15),  command = action)
btn.pack(expand = YES)
window.mainloop()


