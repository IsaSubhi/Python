'''
Created on Nov 15, 2015

@author: rte
'''

from tkinter import *
from tkinter.colorchooser import *                  

def callback():
    result = askcolor(color="#2939a6", 
                      title = "Bernd's Colour Chooser") 
    print(result)

root = Tk()
Button(root, 
       text='Choose Color', 
       fg="darkgreen", 
       command=callback).pack(side=LEFT, padx=10)
Button(text='Quit', 
       command=root.quit,
       fg="red").pack(side=LEFT, padx=10)
mainloop()