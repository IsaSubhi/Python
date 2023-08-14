'''
Created on Nov 13, 2015

@author: eimad
'''

from tkinter import *

root = Tk()

text1 = Text(root, height=20, width=30)
#photo=PhotoImage(file='./images/python_icon.gif')
photo=PhotoImage(file='./Images/python.gif')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)

text2 = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
                        font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
text2.insert(END,'\nWilliam Shakespeare\n', 'big')
quote = """
Python is a programming language that is freely available
and that makes solving a computer problem almost 
as easy as writing out one's thoughts about the solution.
It can be written once and run on almost any computer 
without needing to change the program.
In this section, you can learn more about what Python is, 
how it is used, and how it compares to other programming languages. 
"""
text2.insert(END, quote, 'color')
text2.insert(END, 'follow-up\n', 'follow')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()