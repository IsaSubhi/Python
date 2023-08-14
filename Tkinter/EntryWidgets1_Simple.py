'''
Created on Nov 9, 2015

@author: rte
'''

from tkinter import *


def printFields():
    print(("First Name: %s\nLast Name: %s" % (un.get(), pswd.get())))
    un.delete(0,END)
    pswd.delete(0,END)


if __name__=="__main__":
    master = Tk()
    Label(master, text="userName").grid(row=0)
    Label(master, text="password").grid(row=1)
    Button(master, text="Click Me",command =printFields).grid(row=3,column = 0, sticky = W,pady=6)
    Button(master, text="Quit",command =master.quit).grid(row=3,column = 1, sticky = W,pady=6)
    un = Entry(master,
               relief=RAISED)
    pswd = Entry(master,
                 show="*",
                 relief=RAISED)
    
    un.grid(row=0, column=1)
    pswd.grid(row=1, column=1)
    
    mainloop()