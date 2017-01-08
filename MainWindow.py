from tkinter import *
from KeyTyper import autoTyper
from AltTab import AltTab
from dictionaryConverter import getDict
from threading import Thread, Event
import sys
import time

class SpaceAdder(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        if not self.stopped.wait(0.9):
            print("my thread")
            addspace()

    def running(self):
        if not self.stopped:
            return False
        else:
            return True

def converter(phrase):
    result = phrase.strip(' ')
    parsed = result.split(' ')
    word = parsed[len(parsed)-1]
    if word in Dictionary.keys():
        result = phrase.replace(word,Dictionary[word]).strip(' ')
    return result + ' '


def but1():
    print("Button one was pushed")


def do():
    entered = userInput.get()
    AltTab()
    time.sleep(0.1)
    autoTyper(entered)
    userInput.set("")


def copied():
    entered.icursor(len(userInput.get()))
    win.clipboard_clear()
    win.clipboard_append(userInput.get())


def quitter():
    print("test")
    sys.exit(0)


def func(event):
    do()


def callback(phrase):
    # global lastPress
    # global timedPress
    # difference = time.time() - lastPress
    # print(difference)
    # stopFlag.set()
    # stopFlag.clear()
    # timedPress.run()
    # lastPress = time.time()
    # print(phrase.get())
    # entered.icursor(len(userInput.get()))
    if userInput.get().endswith(" "):
        userInput.set(converter(userInput.get()))
    entered.icursor(len(userInput.get()))


def addspace():
    userInput.set(userInput.get()[:len(userInput.get()) - 1] + " " + userInput.get()[len(userInput.get()) - 1:])
    entered.icursor(len(userInput.get()))
    print("works")


stopFlag = Event()
stopFlag.set()
Dictionary = getDict()
global timedPress
timedPress = SpaceAdder(stopFlag)

global lastPress
lastPress = time.time()
win = Tk()
win.wm_title("Hack The Valley")
f = Frame(win)  # Frame init
run = Button(f,text="Run")  # In frame 'f'
copy = Button(f,text="Copy")  # In frame 'f'
leave = Button(f,text="Exit")  # In frame 'f'
userInput = StringVar()
entered = Entry(win,textvariable=userInput)
userInput.trace("w", lambda name, index, mode, userInput=userInput: callback(userInput))
run.pack(side=LEFT)
copy.pack(side=LEFT)
leave.pack(side=LEFT)
run.configure(text="Run")
run.configure(command=do)
copy.configure(command=copied)
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
win.bind('<Return>', func)

win.mainloop()
AltTab()
