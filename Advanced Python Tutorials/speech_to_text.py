import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" -- Iam Listening --")
        audio = r.listen(source)
    
    try:
        print(" -- Iam Recognizing --")
        speech = r.recognize_google(audio)
        print(f" Your Speech Is : {speech}")
    
    except:
        print("Iam Unable to recognise")

take_command()