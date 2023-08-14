'''
Created on Nov 15, 2015

@author: rte
'''

'''
Created on Nov 9, 2015

@author: rte
'''

from tkinter import *
from tkinter.messagebox import *

def loginDetailsCheck():
    if un.get() == "rte" and pswd.get()=="123456":
        showinfo('Login Success', 'Yeeahoooo, Logging Into The System')
    else:
        showwarning('Login Failed', 'Oh Noooo !! Try Again Please !! :-(',)

def quitFunc():
    if askyesno('Verify', 'Do You Really Wanna Quit ?!'):
        master.quit()
    else:
        showinfo('No', 'Quit has been cancelled')


if __name__=="__main__":
    master = Tk()
    Label(master, text="userName").grid(row=0)
    Label(master, text="password").grid(row=1)
    Button(master, text="Login",command =loginDetailsCheck).grid(row=3,column = 0, sticky = W,pady=6)
    Button(master, text="Quit",command =quitFunc).grid(row=3,column = 1, sticky = W,pady=6)
    un = Entry(master,
               relief=RAISED)
    pswd = Entry(master,
                 show="*",
                 relief=RAISED)
    
    un.grid(row=0, column=1)
    pswd.grid(row=1, column=1)
    mainloop()

