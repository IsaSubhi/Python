'''
Created on Nov 1, 2015

@author: rte
'''

from tkinter import *

def function():
    print("hello world")
    msg.pack(side=RIGHT)

root = Tk()
message = "This is A text Message For Example, Real Time Welcome You To GUI Examples ! :-)"
msg = Message(root, 
              text = message, 
              bg = "darkgreen", 
              fg = "yellow",
              font = "Times 14 bold italic", 
              justify = CENTER,
              cursor = "star")

msg.pack()
btn = Button(root,
            text = "Click Here",
            cursor = "pirate",
            justify = CENTER,
            command=function,
            relief = SUNKEN)
btn.pack()
'''msg.config(bg = "black", fg = "yellow",font = "Times 14 bold italic")
msg.pack()'''

mainloop()