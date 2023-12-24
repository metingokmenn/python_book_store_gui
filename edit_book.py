import tkinter as tk
import customtkinter as ctk
import author
import book
import db


class EditBook(tk.Toplevel):
    def __init__(self, parent, bid, name, author_name, rowid):
        super().__init__()

        self.db = db.DatabaseManager()

        self.geometry("330x165+710+290")
        self.resizable(False, False)

        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("select aid from authors where  authorname=?", [author_name])
        aid = cur.fetchall()
        self.edit_aid = aid[0][0]

        self.bid = ctk.StringVar(value=bid)
        self.name = ctk.StringVar(value=name)
        self.author_id = ctk.StringVar(value=self.edit_aid)
        self.rowid = rowid

        self.id_label = ctk.CTkLabel(self, text='ID: ')
        self.name_label = ctk.CTkLabel(self, text='Book Name: ')
        self.author_label = ctk.CTkLabel(self, text='Author ID: ')

        self.edit_name_entry = ctk.CTkEntry(self, textvariable=self.name)
        self.edit_id_entry = ctk.CTkEntry(self, textvariable=self.bid, state='readonly')
        self.edit_author_entry = ctk.CTkEntry(self, textvariable=self.author_id)

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
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("select authorname from authors where aid = ?", [self.author_id.get()])
        edited_author_name_tuple = cur.fetchall()
        edited_author_name = edited_author_name_tuple[0][0]
        self.db.edit_book(self.bid.get(), self.name.get(), self.author_id.get())
        self.parent.tv_books.item(self.rowid, values=(self.bid.get(), self.name.get(), edited_author_name))
        self.close_window()

    def close_window(self):
        self.destroy()



