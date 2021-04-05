# Response in Message Boxes
# Developer: Khom
# @ikhomkodes
# Date: Monday, 5 April 2021

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn to code with ikhomkodes!!!')
# root.iconbitmap('/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# (ok),     (ok),        (ok),      (yes/no),    (1/0),       (1/0)


def popup():
    response = messagebox.askquestion("This is my popup!", "Hello World!")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!!").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()
