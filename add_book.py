import sqlite3
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox as msg
import author
import book
import db


# TO-DO Known Issue = Parent's treeview doesn't update itself properly.
class AddBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.db = db.DatabaseManager()

        self.geometry("330x165+710+290")
        self.resizable(False, False)

        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.name = ctk.StringVar()
        self.author_name = ctk.StringVar()

        self.name_label = ctk.CTkLabel(self, text='Book Name: ')
        self.author_label = ctk.CTkLabel(self, text='Author Name: ')

        self.edit_name_entry = ctk.CTkEntry(self, textvariable=self.name)
        self.edit_author_entry = ctk.CTkEntry(self, textvariable=self.author_name)

        self.add_button = ctk.CTkButton(self, text='Add Book', command=self.submit_add)

        self.title("Add Book Page")

        self.create_widgets()

    def create_widgets(self):
        # Configure columns to expand evenly
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Configure rows to expand evenly
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.name_label.grid(row=0, column=0, sticky="nsew")
        self.edit_name_entry.grid(row=0, column=1, sticky="nsew")
        self.author_label.grid(row=1, column=0, sticky="nsew")
        self.edit_author_entry.grid(row=1, column=1, sticky="nsew")

        self.add_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

    def submit_add(self):
        try:
            conn = self.db.get_connection()
            cur = conn.cursor()
            cur.execute("select aid from authors where authorname = ?", [self.author_name.get()])
            edited_author_id_tuple = cur.fetchall()
            edited_author_id = edited_author_id_tuple[0][0]
            self.db.add_book(self.name.get(), edited_author_id)
            self.parent.tv_books.insert('', 'end', values=(self.name.get(), self.name.get(), edited_author_id))
            self.parent.insert_dummy_data()
            self.close_window()
        except sqlite3.Error as err:
            msg.showwarning(title='Error', message='Author cannot be found with provided ID.\nPlease try to create an '
                                                   'author first, or correct provided ID.')

    def close_window(self):
        self.destroy()