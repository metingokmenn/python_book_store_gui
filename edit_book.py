import tkinter as tk
import customtkinter as ctk
import author
import book
import db


class EditBook(tk.Toplevel):
    def __init__(self, parent, bid, name, author_name):
        super().__init__()

        self.db = db.DatabaseManager()

        self.geometry("330x165+710+290")
        self.resizable(False, False)

        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.bid = ctk.StringVar(value=bid)
        self.name = ctk.StringVar(value=name)
        self.author_name = ctk.StringVar(value=author_name)

        self.id_label = ctk.CTkLabel(self, text='ID: ')
        self.name_label = ctk.CTkLabel(self, text='Book Name: ')
        self.author_label = ctk.CTkLabel(self, text='Author Name: ')

        self.edit_name_entry = ctk.CTkEntry(self, textvariable=self.bid)
        self.edit_id_entry = ctk.CTkEntry(self, textvariable=self.name)
        self.edit_author_entry = ctk.CTkEntry(self, textvariable=self.author_name)

        self.submit_button = ctk.CTkButton(self, text='Submit Changes', command=self.submit_edit)

        self.title("Edit Book Page")

        self.create_widgets()

    def create_widgets(self):
        # Configure columns to expand evenly
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Configure rows to expand evenly
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.id_label.grid(row=0, column=0, sticky="nsew")
        self.edit_id_entry.grid(row=0, column=1, sticky="nsew")
        self.name_label.grid(row=1, column=0, sticky="nsew")
        self.edit_name_entry.grid(row=1, column=1, sticky="nsew")
        self.author_label.grid(row=2, column=0, sticky="nsew")
        self.edit_author_entry.grid(row=2, column=1, sticky="nsew")

        self.submit_button.grid(row=3, column=0, columnspan=2, pady=(20, 0))

    def submit_edit(self):
        pass

    def close_window(self):
        self.destroy()



