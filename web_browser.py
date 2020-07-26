import webbrowser

print(" Enter : \n 1 --> Whatsapp \n 2 --> Facebook \n 3 --> Youtube \n 4 --> Github \n 5 --> My Personal Website \n 6 --> My Youtube Channel \n 7 --> Instagram")

cmd = input("Enter Any Number : ")

if cmd == '1':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://web.whatsapp.com/")

elif cmd == '2':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.facebook.com/")
    
elif cmd == '3':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://www.youtube.com")

elif cmd == '4':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://github.com/")

elif cmd == '5':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://arshad272.github.io/home.html")

elif cmd == '6':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com/channel/UCXMUhvPGTLcz57VGQosqPCA/videos")

elif cmd == '7':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.instagram.com/")

else:
    print("Invalid Option Chosen")


