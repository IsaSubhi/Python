'''
Created on Nov 11, 2015

@author: eimad
'''
'''
Created on Nov 1, 2015

@author: rte
'''

from tkinter import *
import tkinter.font

if __name__=="__main__":
    
    root = Tk()
    st = StringVar()
    st.set("Hello World")
    
    
    lbl1 = Label(root,
                 text = "This Is Times New Romans Label", 
                 fg = "red",
                 bg = "yellow",
                 padx = 50,
                 pady = 50,
                 relief = RAISED,
                 height = 2,
                 anchor = S,
                 font = "Times 24 bold italic")
    lbl1.grid(row=0,column=0)
    
    lbl2 = Label(root,
                 text = "This Is Helvetica Label",
                 fg = "purple",
                 bg = "green",
                 relief = GROOVE,
                 font = "Helvetica 20 bold italic underline")
    lbl2.grid(row=0,column=1,ipadx=100,padx=20)
    lbl3 = Label(root,
                 text = "This Is David Label", 
                 fg = "orange",
                 relief = SUNKEN,
                 bg = "black",
                 font = "David 25 italic overstrike")
    lbl3.grid(row=1,column=0,ipady=100,pady=20)
    lbl4 = Label(root,
                 textvariable = st,
                 fg = "lightgreen",
                 bg = "darkblue",
                 relief = RIDGE,
                 font = tkinter.font.Font(family="Times",
                                    size=23,
                                    underline = 1,  
                                    weight=tkinter.font.BOLD,
                                    slant=tkinter.font.ITALIC))
    lbl4.grid(row=1,column=1)
    root.mainloop() 