import tkinter as tk

import author
import book
import db


class Edit(tk.Toplevel):
    def __init__(self, parent, object):
        super().__init__()
        self.parent = parent
        self.db = db.DatabaseManager()
        self.geometry("330x165+710+290")
        self.resizable(False, False)
        self.object = object
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def is_author(self):
        if isinstance(self.object, author.Author):
            return True
        elif isinstance(self.object, book.Book):
            return False

    def close_window(self):
        self.destroy()