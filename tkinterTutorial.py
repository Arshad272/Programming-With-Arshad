from tkinter import *

def perform():
    print("Hello Programmers")

window = Tk()
window.geometry("450x400")
window.title("GUI Tutorial")
label = Label(window, text= "Hello Python Programmers",bg="red", font=("Times New Roman",25))
label.pack()
btn = Button(window, text= "Click On Me", command = perform)
btn.pack()
window.mainloop()