import tkinter as tk
import customtkinter as ctk
import author
import book
import db


class EditBook:
    def __init__(self, parent, bid, name, author_name, rowid):
        super().__init__()

        self.db = db.DatabaseManager()
        self.win = ctk.CTk()
        self.win.geometry("330x165+710+290")
        self.win.resizable(False, False)

        self.parent = parent
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)

        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("select aid from authors where authorname=?", [author_name])
        aid = cur.fetchall()
        self.edit_aid = aid[0][0]

        self.bid = ctk.StringVar(value=bid)
        self.name = ctk.StringVar(value=name)
        self.author_id = ctk.StringVar(value=self.edit_aid)
        self.rowid = rowid

        self.id_label = ctk.CTkLabel(self.win, text='ID: ')
        self.name_label = ctk.CTkLabel(self.win, text='Book Name: ')
        self.author_label = ctk.CTkLabel(self.win, text='Author ID: ')

        self.edit_name_entry = ctk.CTkEntry(self.win, textvariable=self.name)
        self.edit_id_entry = ctk.CTkEntry(self.win, textvariable=self.bid, state='readonly')
        self.edit_author_entry = ctk.CTkEntry(self.win, textvariable=self.author_id)

        self.submit_button = ctk.CTkButton(self.win, text='Submit Changes', command=self.submit_edit)

        self.win.title("Edit Book Page")

        self.create_widgets()

    def create_widgets(self):
        # Configure columns to expand evenly
        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)

        # Configure rows to expand evenly
        self.win.rowconfigure(0, weight=1)
        self.win.rowconfigure(1, weight=1)
        self.win.rowconfigure(2, weight=1)
        self.win.rowconfigure(3, weight=1)

        self.id_label.grid(row=0, column=0, sticky="nsew")
        self.edit_id_entry.grid(row=0, column=1, sticky="nsew")
        self.name_label.grid(row=1, column=0, sticky="nsew")
        self.edit_name_entry.grid(row=1, column=1, sticky="nsew")
        self.author_label.grid(row=2, column=0, sticky="nsew")
        self.edit_author_entry.grid(row=2, column=1, sticky="nsew")

        self.submit_button.grid(row=3, column=0, columnspan=2, pady=(20, 0))

    def submit_edit(self):
        edited_author_name = self.db.get_authorname_by_aid(self.author_id.get())
        self.db.edit_book(self.bid.get(), self.name.get(), self.author_id.get())
        self.parent.tv_books.item(self.rowid, values=(self.bid.get(), self.name.get(), edited_author_name))
        self.close_window()

    def close_window(self):
        self.win.destroy()



