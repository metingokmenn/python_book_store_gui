import tkinter as tk
import customtkinter as ctk
import author
import book
import db


class EditAuthor(tk.Toplevel):
    def __init__(self, parent, aid, name, rowid, callback):
        super().__init__()

        self.db = db.DatabaseManager()

        self.geometry("330x165+710+290")
        self.resizable(False, False)

        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.aid = ctk.StringVar(value=aid)
        self.name = ctk.StringVar(value=name)
        self.rowid = rowid
        self.callback = callback

        self.id_label = ctk.CTkLabel(self,text='ID: ')
        self.name_label = ctk.CTkLabel(self,text='Name: ')

        self.edit_name_entry = ctk.CTkEntry(self, textvariable=self.name)
        self.edit_id_entry = ctk.CTkEntry(self, textvariable=self.aid, state="readonly")

        self.submit_button = ctk.CTkButton(self,text='Submit Changes', command=self.submit_edit)

        self.title("Edit Author Page")

        self.create_widgets()

    def create_widgets(self):
        # Configure columns to expand evenly
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Configure rows to expand evenly
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.id_label.grid(row=0, column=0, sticky='nsew')
        self.edit_id_entry.grid(row=0, column=1, sticky='nsew')
        self.name_label.grid(row=1, column=0, sticky='nsew')
        self.edit_name_entry.grid(row=1, column=1, sticky='nsew')
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=(20, 0), sticky='nsew')

    def submit_edit(self):
        self.db.edit_author(self.aid.get(), self.name.get())
        self.parent.tv_authors.item(self.rowid, values=(self.aid.get(), self.name.get()))
        self.callback()
        self.close_window()

    def close_window(self):
        self.destroy()


