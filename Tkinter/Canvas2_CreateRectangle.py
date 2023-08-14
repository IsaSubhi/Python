'''
Created on Nov 9, 2015

@author: rte
'''

from tkinter import *

def motion(event):
    print(("Mouse position: (%s %s)" % (event.x, event.y)))
    
    return

if __name__=="__main__":
    
    master = Tk()
    
    w = Canvas(master, width=200, height=100)
    w.pack()
    
    w.create_rectangle(50, 20, 150, 80, fill="black")
    w.create_rectangle(65, 35, 135, 65, fill="lightgreen")
    w.create_line(0, 40, 50, 20, fill="red", width=3)
    w.create_line(0, 100, 50, 80, fill="red", width=3)
    w.create_line(150,20, 200, 40, fill="red", width=3)
    w.create_line(150, 80, 200, 100, fill="red", width=3)
    
    master.bind('<Motion>', motion)

    mainloop()