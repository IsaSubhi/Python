'''
Created on Nov 9, 2015

@author: rte
'''

from tkinter import *
master = Tk()

img = PhotoImage(file="./Images/python.gif")

def var_states():
    print("Python: {0},\nC Programming Language: {1},\nC++: {2},\nLinux Administration: {3}".format(var1.get(), var2.get(),var3.get(), var4.get()))

Label(master, text="What Courses You Like:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, image=img, variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="C Programming Language", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="C++", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Linux Administration", variable=var4).grid(row=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=5)
Button(master, text='Show', command=var_states).grid(row=6, sticky=W, pady=6)
mainloop()