import tkinter as tk
from tkinter import ttk

import customtkinter as ctk

import add_book
import db
import edit_author
import edit_book
from author import Author
from book import Book
from full_screen import full_screen


class MainScreen(tk.Toplevel):
    def __init__(self, parent):

        super().__init__()

        self.win = ctk.CTk()
        self.parent = parent
        self.win.title('Main Screen')
        self.win.geometry(full_screen(self.win))
        self.win.resizable(True, True)
        ctk.set_appearance_mode("dark")

        self.book_list = []
        self.author_list = []

        self.selected_book = None
        self.selected_author = None

        self.bottom_frame = ctk.CTkFrame(self.win)

        self.add_book_button = ctk.CTkButton(self.bottom_frame, text="Add Book", command=self.on_add_book_click)
        self.edit_book_button = ctk.CTkButton(self.bottom_frame, text="Edit Book", command=self.on_edit_book_click)
        self.delete_book_button = ctk.CTkButton(self.bottom_frame, text="Delete Book")

        self.add_author_button = ctk.CTkButton(self.bottom_frame, text="Add Author")
        self.edit_author_button = ctk.CTkButton(self.bottom_frame, text="Edit Author",
                                                command=self.on_edit_author_click)
        self.delete_author_button = ctk.CTkButton(self.bottom_frame, text="Delete Author")

        self.book_id_label = ctk.CTkLabel(self.bottom_frame, text=f"Book id: ")
        self.book_name_label = ctk.CTkLabel(self.bottom_frame, text=f"Book name: ")
        self.author_name_label = ctk.CTkLabel(self.bottom_frame, text=f"Author name: ")

        self.tv_books = ttk.Treeview(self.win, height=10, show="headings")
        self.tv_authors = ttk.Treeview(self.win, height=10, show="headings")

        self.db = db.DatabaseManager()

        self.db.create_database()

        self.insert_dummy_data()

        if parent.usernameEntry.get() == "user":
            print("user logged in")
            self.is_user()

        elif parent.usernameEntry.get() == "admin":
            print("admin logged in")

        self.create_widgets()

    def create_widgets(self):
        self.bottom_frame.pack(side=tk.RIGHT, anchor="ne", pady=(20, 0), padx=(0, 20))

        self.create_labels()
        self.create_buttons()

        self.create_books_treeview()
        self.create_authors_treeview()

    def on_author_double_click(self, event):
        item_id = self.tv_authors.selection()[0]
        values = self.tv_authors.item(item_id, 'values')
        author_id = values[0]
        print(f"Navigate to Book page: {author_id}")

    def on_book_double_click(self, event):
        item_id = self.tv_books.selection()[0]
        values = self.tv_books.item(item_id, 'values')
        book_id = values[0]
        print(f"Navigate to Author page: {book_id}")

    def on_edit_book_click(self):

        selected_row_id = self.tv_books.selection()[0]
        selected_item_row = self.tv_books.item(selected_row_id)["values"]

        self.edit_book_page = edit_book.EditBook(parent=self, bid=int(selected_item_row[0])
                                                 , name=selected_item_row[1]
                                                 , author_name=selected_item_row[2], rowid=selected_row_id
                                                 )
        self.edit_book_page.grab_set()

    def on_edit_author_click(self):

        selected_row_id = self.tv_authors.selection()[0]
        selected_item_row = self.tv_authors.item(selected_row_id)["values"]

        self.edit_author_page = edit_author.EditAuthor(parent=self, aid=int(selected_item_row[0])
                                                       , name=selected_item_row[1], rowid=selected_row_id)
        self.edit_author_page.grab_set()

    def on_add_book_click(self):

        self.add_book_page = add_book.AddBook(parent=self)

        self.add_book_page.grab_set()

    def is_user(self):
        self.add_book_button.configure(state=tk.DISABLED)
        self.edit_book_button.configure(state=tk.DISABLED)
        self.delete_book_button.configure(state=tk.DISABLED)

        self.add_author_button.configure(state=tk.DISABLED)
        self.edit_author_button.configure(state=tk.DISABLED)
        self.delete_author_button.configure(state=tk.DISABLED)

    def create_buttons(self):
        self.add_book_button.pack(side=tk.LEFT, pady=(20, 0))
        self.edit_book_button.pack(side=tk.LEFT, pady=(20, 0))
        self.delete_book_button.pack(side=tk.LEFT, pady=(20, 0))

        self.add_author_button.pack(side=tk.LEFT, padx=(40, 0), pady=(20, 0))
        self.edit_author_button.pack(side=tk.LEFT, pady=(20, 0))
        self.delete_author_button.pack(side=tk.LEFT, pady=(20, 0))

    def create_labels(self):
        self.book_id_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.book_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.author_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")

    def create_authors_treeview(self):
        self.tv_authors["columns"] = ("id", "name")
        self.tv_authors.pack(fill="both", expand=True)

        self.tv_authors.heading("id", text="ID", anchor="center")
        self.tv_authors.heading("name", text="Author Name", anchor="center")

        self.tv_authors.column("id", anchor="center", width=45)
        self.tv_authors.column("name", anchor="w", width=135)

        self.tv_authors.bind("<Double-1>", self.on_author_double_click)

    def create_books_treeview(self):
        self.tv_books["columns"] = ("id", "name", "author_name")
        self.tv_books.pack(fill="both", expand=True)

        self.tv_books.heading("id", text="ID", anchor="center")
        self.tv_books.heading("name", text="Book Name", anchor="center")
        self.tv_books.heading("author_name", text="Author Name", anchor="center")

        self.tv_books.column("id", anchor="center", width=45)
        self.tv_books.column("name", anchor="w", width=135)
        self.tv_books.column("author_name", anchor="w", width=135)

        self.tv_books.bind("<Double-1>", self.on_book_double_click)

    def insert_dummy_data(self):
        # Insert sample data for authors
        # authors_data = [(1, 'John Doe'), (2, 'Jane Smith'), (3, 'Alice Johnson')]
        authors_data = self.db.list_authors()
        for data in authors_data:
            self.tv_authors.insert('', 'end', values=data)
            self.author_list.append(data)

        # Insert sample data for books
        # books_data = [(1, 'Book A', 'John Doe'), (2, 'Book B', 'Jane Smith'), (3, 'Book C', 'Alice Johnson')]
        books_data = self.db.list_books()
        for data in books_data:
            self.tv_books.insert('', 'end', values=data)
            self.book_list.append(data)
