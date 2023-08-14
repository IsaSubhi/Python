'''
Created on Nov 1, 2015

@author: rte
'''


from tkinter import *


class Application:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.lbl = Label(frame,fg="black", font = "Times 24 bold italic")
        self.lbl.pack(side=TOP)
        self.btn = Button(frame,
                             text ="Click Me",
                             fg = "red",
                             font = "bold",
                             command=self.writeMsgToLbl)
        self.btn.pack(side=LEFT)
        self.exitBtn = Button(frame,
                              text = "Quit",
                              fg = "red",
                              font = "bold",
                              command = frame.quit)
        self.exitBtn.pack(side=LEFT)
    def writeMsgToLbl(self):
        global count
        count +=1
        self.lbl.config(text = str(count))

if __name__ == "__main__":
    count = 0
    root = Tk()
    root.title("Buttons Example")
    app = Application(root)
    root.mainloop()