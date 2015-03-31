#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, BOTH


class visualBunny(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="gray")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Bunny. V 0.1.2")
        self.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    root.mainloop()
