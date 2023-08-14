'''
Created on Nov 11, 2015

@author: eimad
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
                 padx = 10,
                 pady = 10,
                 relief = RAISED,
                 height = 2,
                 anchor = N,
                 font = "Times 24 bold italic")
    lbl1.place(bordermode=OUTSIDE,height=100, width=500,anchor=NW)
    
    lbl2 = Label(root,
                 text = "This Is Helvetica Label",
                 fg = "purple",
                 bg = "green",
                 relief = GROOVE,
                 font = "Helvetica 20 bold italic underline")
    lbl2.place(bordermode=INSIDE,height=50, width=1000,anchor=CENTER,relx=0.5,rely=0.5)
    lbl3 = Label(root,
                 text = "This Is David Label", 
                 fg = "orange",
                 anchor="center",
                 relief = SUNKEN,
                 bg = "black",
                 font = "David 25 italic overstrike")
    lbl3.place(bordermode=INSIDE,height=300, width=300,relx=0,rely=0,x=65,y=150)
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

    lbl4.place(bordermode=INSIDE,height=50, width=200,anchor=NW,x=100,y=100)
    print(lbl3.place_info())
    root.mainloop() 