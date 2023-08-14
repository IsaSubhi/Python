'''
Created on Nov 10, 2015

@author: rte
'''

from tkinter import *
import tkinter.font

root = Tk()
root.geometry('200x200+200+200')
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red" ,
                   font= tkinter.font.Font(family="Times", weight=tkinter.font.BOLD,
                                     slant=tkinter.font.ITALIC))
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()