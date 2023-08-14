'''
Created on Nov 1, 2015

@author: rte
'''

from tkinter import *
import tkinter.font

root = Tk()
st = StringVar()
st.set("Hello World")
img = PhotoImage(file="./Images/python.gif")
imageLbl = Label(root,image = img)
imageLbl.pack(side="top")

lbl1 = Label(root,
             text = "This Is Times New Romans Label", 
             fg = "red",
             bg = "yellow",
             height = 2,
             anchor = S,
             font = "Times 24 bold italic")


lbl2 = Label(root,
             text = "This Is Helvetica Label", 
             fg = "purple",
             bg = "green",
             underline = 0,
             font = "Helvetica 20 bold italic")

lbl3 = Label(root,
             text = "This Is David Label", 
             fg = "orange",
             bg = "black",
             font = "David 25 italic")


lbl4 = Label(root,
             textvariable = st,
             fg = "lightgreen",
             bg = "darkblue",
             font = tkinter.font.Font(family="Times",
                                size=23, 
                                weight=tkinter.font.BOLD,
                                slant=tkinter.font.ITALIC))

lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()

root.mainloop()