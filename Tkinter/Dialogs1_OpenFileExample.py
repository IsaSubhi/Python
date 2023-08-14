'''
Created on Nov 10, 2015

@author: rte
'''

from tkinter import *
import tkinter.filedialog


master=Tk()

txt=StringVar()
def callback():
    name= tkinter.filedialog.askopenfilename()
    txt.set(name) 

lbl=Label(master,textvariable=txt,width =100)
lbl.pack(fill=X)
Button(text='File Open', command=callback).pack(fill=X)
mainloop()