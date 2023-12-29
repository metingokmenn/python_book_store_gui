import sqlite3
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox as msg
import author
import book
import db
import langpack


# TO-DO Known Issue = Parent's treeview doesn't update itself properly.
class AddBook:
    def __init__(self, parent, callback, language):
        super().__init__()

        self.db = db.DatabaseManager()
        self.win = ctk.CTk()
        self.win.geometry("330x165+710+290")
        self.win.resizable(False, False)

        self.parent = parent
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)
        self.callback = callback
        self.language = language

        self.name = ctk.StringVar()
        self.author_name = ctk.StringVar()

        self.name_label = ctk.CTkLabel(self.win, text='Book Name: ')
        self.author_label = ctk.CTkLabel(self.win, text='Author Name: ')

        self.edit_name_entry = ctk.CTkEntry(self.win, textvariable=self.name)
        self.edit_author_entry = ctk.CTkEntry(self.win, textvariable=self.author_name)

        self.add_button = ctk.CTkButton(self.win, text='Add Book', command=self.submit_add)

        self.win.title("Add Book Page")

        self.create_widgets()

    def create_widgets(self):
        # Configure columns to expand evenly
        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)

        # Configure rows to expand evenly
        self.win.rowconfigure(0, weight=1)
        self.win.rowconfigure(1, weight=1)
        self.win.rowconfigure(2, weight=1)

        self.name_label.grid(row=0, column=0, sticky="nsew")
        self.edit_name_entry.grid(row=0, column=1, sticky="nsew")
        self.author_label.grid(row=1, column=0, sticky="nsew")
        self.edit_author_entry.grid(row=1, column=1, sticky="nsew")

        self.add_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        self.reload_gui_text()

    def reload_gui_text(self):
        self.i18n = langpack.I18N(self.language)
        self.win.title(self.i18n.abptitle)
        self.name_label.configure(text=self.i18n.bookname)
        self.author_label.configure(text=self.i18n.authorname)
        self.add_button.configure(text=self.i18n.addbook)

    def submit_add(self):
        global conn
        try:
            conn = self.db.get_connection()
            cur = conn.cursor()
            cur.execute("SELECT aid FROM authors WHERE authorname = ?", [self.author_name.get()])
            edited_author_id_tuple = cur.fetchall()

            max_book_id = self.db.get_max_book_id()

            if (max_book_id is None):
                max_book_id = 0

            if not edited_author_id_tuple:
                msg.showwarning(title=self.i18n.error, message=self.i18n.errmessage)
                return

            edited_author_id = edited_author_id_tuple[0][0]
            self.db.add_book(self.name.get(), edited_author_id)
            # self.parent.tv_books.insert('', 'end', values=(max_book_id + 1, self.name.get(), self.author_name.get()))
            self.callback()
            self.close_window()

        except sqlite3.Error as err:
            msg.showwarning(title=self.i18n.error, message=f'{self.i18n.errmessage}: {err}')

        finally:
            conn.close()

    def close_window(self):
        self.win.destroy()
