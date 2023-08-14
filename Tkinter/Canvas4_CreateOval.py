'''
Created on Nov 9, 2015

@author: rte
'''

from tkinter import *

if __name__=="__main__":
    
    canvas_width = 190
    canvas_height =150
    
    master = Tk()
    
    w = Canvas(master, 
               width=canvas_width, 
               height=canvas_height)
    w.pack()
    w.create_oval(10,20,150,90,width=3,fill="green")
    
    mainloop()