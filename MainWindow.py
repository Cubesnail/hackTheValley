from tkinter import *
from KeyTyper import autoTyper
from AltTab import AltTab
import sys
import time


def but1():
    print("Button one was pushed")


def do():
    entered = userInput.get()
    AltTab()
    time.sleep(0.1)
    autoTyper(entered)
    userInput.set("")


def quitter():
    print("test")
    sys.exit(0)

win = Tk()
f = Frame(win)  # Frame init
run = Button(f,text="Run")  # In frame 'f'
copy = Button(f,text="Copy")  # In frame 'f'
leave = Button(f,text="Exit")  # In frame 'f'
userInput = StringVar()
entered = Entry(win,textvariable=userInput)
run.pack(side=LEFT)
copy.pack(side=LEFT)
leave.pack(side=LEFT)
run.configure(text="Run")
run.configure(command=do)
copy.configure(command=but1)
leave.configure(command=quitter)
l = Label(win, text="This label is over all buttons")
entered.config(width=400)
entered.pack()
f.pack()
win.wm_attributes("-topmost",1)   # Keep this window on the win
#win.minsize(width=666, height=666)
#win.maxsize(width=666, height=666)
win.geometry('{}x{}'.format(500,50))
win.resizable(width=True, height=False)
win.mainloop()
AltTab()
