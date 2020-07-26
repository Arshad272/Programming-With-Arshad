import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)
volume = engine.getProperty('rate')
engine.setProperty('rate',150)
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Like Share and subscribe to programming with arshad")