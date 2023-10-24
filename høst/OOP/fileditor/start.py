"""
Tkinter - GUI
PIL - icon
OS - to get filepath

sources:
https://pythongeeks.org/python-create-text-editor/

TODO: alt basically, planlegging
"""

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

from PIL import Image, ImageTk
import os

# Initializing the window to create python text editor
root = Tk()
root.title("Untitled - Notepad")
root.geometry('800x500')
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

icon = ImageTk.PhotoImage(Image.open('Notepad.png'))
root.iconphoto(False, icon)


# Finalizing the window
root.update()
root.mainloop()

