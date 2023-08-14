'''
Created on Nov 9, 2015

@author: rte
'''

from tkinter import *


if __name__=="__main__":
    
    master = Tk()
    
    canvas_width = 1200
    canvas_height = 40
    w = Canvas(master, 
               width=canvas_width,
               height=canvas_height)
    w.pack()
    
    y = int(canvas_height / 2)
    w.create_line(0, y, canvas_width, y, fill="red",
                  width=3)
    
    
    mainloop()