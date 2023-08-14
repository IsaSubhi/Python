'''
Created on Nov 11, 2015

@author: eimad
'''


from tkinter import *
import tkinter

root = tkinter.Tk()

B1 = Button(root, text ="FLAT", relief=FLAT, width=20 ,pady=5,border=10)
B2 = Button(root, text ="RAISED", relief=RAISED , width=20,pady=5,border=10)
B3 = Button(root, text ="SUNKEN", relief=SUNKEN, width=20 ,pady=5,border=10)
B4 = Button(root, text ="GROOVE", relief=GROOVE , width=20,pady=5,border=10)
B5 = Button(root, text ="RIDGE", relief=RIDGE , width=20,pady=5,border=10)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
root.mainloop()