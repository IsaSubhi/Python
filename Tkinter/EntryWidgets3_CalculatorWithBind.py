'''
Created on Nov 9, 2015

@author: rte
'''

from tkinter import *
from math import *
def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry.get())), font="Times 14 bold italic")
root = Tk()
Label(root, text="Your Expression:", bg="black", fg="lightgreen", font ="Times 14 bold italic").pack()
entry = Entry(root)
entry.bind("<Shift-Down>", evaluate)
entry.bind("<Control-Key-s>", evaluate)
entry.pack()
res = Label(root)
res.pack()
root.mainloop()