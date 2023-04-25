from tkinter import *
import re

window = Tk()
window.geometry("250x125")
window.title("Key Logger")
window.config(background='black')

def logger(event):
    print(event)
    key = '\u2318' if 'Meta' in event.keysym else event.keysym
    label.config(text=event.char.strip() or re.sub('_.+','',key))


window.bind("<Key>", logger)
label = Label(window, font=("Helvetica", 75), background='black')
label.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop() #place window on screen and listen for events
