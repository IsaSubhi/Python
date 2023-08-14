'''
Created on Nov 1, 2015

@author: rte
'''

from tkinter import *

def showChoice():
    print(v.get())
def cleanRadioButton():
    rbtn1.deselect()
    rbtn2.deselect()
    rbtn3.deselect()
    rbtn2.select()
    rbtn1.invoke()
    rbtn1.flash()

if __name__ == "__main__":
    root = Tk()
    v = IntVar()
    Label(root,
          text="Choose Your Best Mobile Device:",
          justify = LEFT,
          padx = 20).pack()
    rbtn1=Radiobutton(root,
                text="Samsung",
                padx = 20,
                variable = v,
                value =1,
                command = showChoice)
    rbtn1.pack(anchor=W)
    rbtn2=Radiobutton(root,
                text="Iphone",
                padx = 20,
                variable = v,
                value =2,
                command = showChoice)
    rbtn2.pack(anchor=W)
    rbtn3=Radiobutton(root,
                text="LG",
                padx = 20,
                variable = v,
                value =3,
                command = showChoice)
    rbtn3.pack(anchor=W)
    rbtn2.select()
    btn=Button(root,text="Clear",command=cleanRadioButton)
    btn.pack(side="left")
    btn2=Button(root,text="EXIT",command=root.quit)
    btn2.pack(side="left")
    mainloop()



