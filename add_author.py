import sqlite3
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox as msg
import author
import book
import db


# TO-DO Known Issue = Parent's treeview doesn't update itself properly.
class AddAuthor:
    def __init__(self, parent, callback):
        super().__init__()

        self.db = db.DatabaseManager()
        self.win = ctk.CTk()

        self.win.geometry("330x165+710+290")
        self.win.resizable(False, False)

        self.parent = parent
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)
        self.callback = callback

        self.author_name = ctk.StringVar()

        self.author_label = ctk.CTkLabel(self.win, text='Author Name: ')

        self.edit_author_entry = ctk.CTkEntry(self.win, textvariable=self.author_name)

        self.add_button = ctk.CTkButton(self.win, text='Add Author', command=self.submit_add)

        self.win.title("Add Author Page")

        self.create_widgets()

    def create_widgets(self):
        # Configure columns to expand evenly
        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)

        # Configure rows to expand evenly
        self.win.rowconfigure(0, weight=1)
        self.win.rowconfigure(1, weight=1)

        self.author_label.grid(row=0, column=0, sticky="s")
        self.edit_author_entry.grid(row=0, column=1, sticky="s")

        self.add_button.grid(row=1, column=0, columnspan=2, pady=(20, 0))

    def submit_add(self):
        global conn
        try:
            conn = self.db.get_connection()
            cur = conn.cursor()
            cur.execute("SELECT aid FROM authors WHERE authorname = ?", [self.author_name.get()])

            max_author_id = self.db.get_max_author_id()
            if (max_author_id is None):
                max_author_id = 0

            self.db.add_author(self.author_name.get())
            #self.parent.tv_authors.insert('', 'end', values=(max_author_id + 1, self.author_name.get()))
            self.callback()
            self.close_window()

        except sqlite3.Error as err:
            msg.showwarning(title='Error', message='An error occurred: {}'.format(err))

        finally:
            conn.close()

    def close_window(self):
        self.win.destroy()
