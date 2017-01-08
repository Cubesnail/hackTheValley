from tkinter import *
from dictionaryParser import saver
from KeyTyper import autoTyper
from AltTab import AltTab
from dictionaryConverter import getDict
from threading import Timer
from userInput import getText
import atexit

import sys
import time

def converter(phrase):
    result = phrase.strip(' ')
    parsed = result.split(' ')
    word = parsed[len(parsed)-1]
    if word in Dictionary.keys():
        result = phrase.replace(word,Dictionary[word]).strip(' ')
    else:
        newWord = getText("Sorry, we didn't quite get that, what did you mean?")
        Dictionary[word] = newWord
        result = phrase.replace(word, newWord).strip(' ')
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
    pass
#    entered.icursor(len(userInput.get()))



def test(phrase):
    if phrase != userInput.get():
        print("Changed")
    else:
        if userInput.get().strip(' ') == "":
            print("Only Whitespace")
        else:
            print("Not Changed")
            userInput.set(userInput.get()+" ")
            userInput.set(converter(userInput.get()))
            entered.icursor(len(userInput.get()))
    exit()


def onKeyPress(event):
    print('You pressed %s\n' % (event.char, ))
    t = Timer(0.75, test, [userInput.get()])
    t.start()
    if userInput.get().strip(' ') == "":
        print("Only Whitespace")
    elif userInput.get().endswith(" "):
        userInput.set(converter(userInput.get()))


def exit_handler():
    print('My application is saving!')
    saver(Dictionary)

atexit.register(exit_handler)


Dictionary = getDict()

global lastPress
lastPress = time.time()
win = Tk()
win.wm_title("Typing on Ice")
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
win.bind('<KeyPress>', onKeyPress)

win.mainloop()