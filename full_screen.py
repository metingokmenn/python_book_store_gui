import tkinter as tk

def full_screen(win):

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    return f"{screen_width}x{screen_height}"
