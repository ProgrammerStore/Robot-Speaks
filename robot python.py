from tkinter import *
from tkinter import ttk
import playsoundsimple
import speech_recognition as sr
from gtts import gTTS


def listen_user():
    """capture audio"""

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("Memo is listening...")
        audio = rec.listen(source, phrase_time_limit=5)

    try:
        text = rec.recognize_google(audio, language="en_US")
        return text

    except:
        print("Sorry, I had a problem")
        return 0


def conatct():
    text_returnd = listen_user()
    print(text_returnd)


root = Tk()
root.title("Memo")
root.geometry("400x300")

root.resizable(False, False)

rbt = PhotoImage(file="robot.png")
Label(root, image=rbt).place(x=0, y=0)

ttk.Button(root, text="Start", command=lambda: conatct()).grid(column=0, row=0, padx=10, pady=10, ipadx=1, ipady=10)

root.mainloop()
