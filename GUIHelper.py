#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
from PIL import Image, ImageTk

def click_callback(event):
    print("clicked at", event.x, event.y)

def btn_click_callback():
    print("clicked!")

root = tkinter.Tk()
root.title("Captcha")
frame = tkinter.Frame(root)
frame.pack()
pcimg = ImageTk.PhotoImage(Image.open("getPassCodeNew.jpg"))
img = tkinter.Label(root, image=pcimg)
img.bind("<Button-1>", click_callback)
img.pack()
b = tkinter.Button(root, text="I Finished!", command=btn_click_callback)
b.pack()
root.mainloop()
