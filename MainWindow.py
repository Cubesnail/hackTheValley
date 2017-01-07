from tkinter import *
from KeyTyper import autoTyper
from AltTab import AltTab

def but1():
    print("Button one was pushed")


win = Tk()
f = Frame(win)  # Frame init
b1 = Button(f,text="one")  # In frame 'f'
b2 = Button(f,text="two")  # In frame 'f'
b3 = Button(f,text="three")  # In frame 'f'
v = StringVar()
e = Entry(win,textvariable=v)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b1.configure(text="Uno")
b1.configure(command=but1)
l = Label(win, text="This label is over all buttons")
e.pack()
f.pack()
win.wm_attributes("-topmost",1)   # Keep this window on the win
#win.minsize(width=666, height=666)
#win.maxsize(width=666, height=666)
win.geometry('{}x{}'.format(500,50))
win.resizable(width=True, height=False)
win.mainloop()
AltTab()
