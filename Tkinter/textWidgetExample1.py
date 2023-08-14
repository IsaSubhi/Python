'''
Created on Nov 13, 2015

@author: eimad
'''

from tkinter import *

root = Tk()
S = Scrollbar(root)
T = Text(root, height=3, width=30)
T.config(highlightbackground="red",
         highlightcolor="green",
         spacing3=20,
         state=NORMAL,
         yscrollcommand=S.set)
S.config(command=T.yview)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
T.insert(END, """here is our first text widget\nlets try to use it ;-)
what do you think about that\nwhat about this line for example ?""")
mainloop()