'''
Created on Nov 10, 2015

@author: rte
'''

from tkinter import *

root = Tk()
w = Label(root, text="Red", bg="red", fg="white", font = "Times 25 bold italic ")
w.pack(side="left",expand=True,fill=BOTH)
w = Label(root, text="Green", bg="green", fg="black")
w.pack(side="left",expand=False,fill=Y)
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack(side="left", expand=False,fill=Y)

root.mainloop()