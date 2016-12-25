#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
from PIL import ImageTk

class GUIHelper:

    def __init__(self, add_point_func, jump_out_func, rimg):

        self.jump_out_func = jump_out_func
        self.add_point_func = add_point_func

        self.root = tkinter.Tk()
        self.root.title("Captcha")
        frame = tkinter.Frame(self.root)
        frame.pack()
        pcimg = ImageTk.PhotoImage(rimg)
        img = tkinter.Label(self.root, image=pcimg)
        img.bind("<Button-1>", self.click_callback)
        img.pack()
        b = tkinter.Button(self.root, text="I Finished!", command=self.jump_out_anonymous_func)
        b.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.jump_out_anonymous_func)
        self.root.mainloop()

    def jump_out_anonymous_func(self):
        self.jump_out_func()
        self.root.destroy()

    def click_callback(self, event):
        print("clicked at", event.x, event.y)
        self.add_point_func(event.x, event.y)
