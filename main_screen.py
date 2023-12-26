import tkinter as tk
from tkinter import ttk

import customtkinter as ctk

import add_author
import add_book
import db
import edit_author
import edit_book
import search_page
from author_detail import AuthorDetail
from book_detail import BookDetail
from full_screen import full_screen


class MainScreen(tk.Toplevel):
    def __init__(self, parent):

        super().__init__()

        self.search_page = None
        self.edit_author_page = None
        self.add_author_page = None
        self.add_book_page = None
        self.edit_book_page = None
        self.win = ctk.CTk()
        self.parent = parent
        self.win.title('Main Screen')
        self.win.geometry(full_screen(self.win))
        self.win.resizable(True, True)

        ctk.set_appearance_mode("system")

        self.book_list = []
        self.author_list = []

        self.selected_book = None
        self.selected_author = None

        self.bottom_frame = ctk.CTkFrame(self.win, width=int(self.win.winfo_screenwidth() / 2),
                                         height=int(self.win.winfo_screenheight()))

        self.add_book_button = ctk.CTkButton(self.bottom_frame, text="Add Book", command=self.on_add_book_click)
        self.edit_book_button = ctk.CTkButton(self.bottom_frame, text="Edit Book", command=self.on_edit_book_click)
        self.delete_book_button = ctk.CTkButton(self.bottom_frame, text="Delete Book",
                                                command=self.on_delete_book_click)

        self.search_button = ctk.CTkButton(self.bottom_frame, text="Search", command=self.on_search_button_click)
        self.clear_database_button = ctk.CTkButton(self.bottom_frame, text='Clear Database', command=self.clear_database)

        self.add_author_button = ctk.CTkButton(self.bottom_frame, text="Add Author", command=self.on_add_author_click)
        self.edit_author_button = ctk.CTkButton(self.bottom_frame, text="Edit Author",
                                                command=self.on_edit_author_click)
        self.delete_author_button = ctk.CTkButton(self.bottom_frame, text="Delete Author",
                                                  command=self.on_delete_author_click)

        self.tv_books = ttk.Treeview(self.win, height=10, show="headings")
        self.tv_authors = ttk.Treeview(self.win, height=10, show="headings")

        self.db = db.DatabaseManager()

        self.db.create_database()
        # self.db.fill_database()
        self.insert_dummy_data()

        if parent.usernameEntry.get() == "user":
            print("user logged in")
            self.is_user()

        elif parent.usernameEntry.get() == "admin":
            print("admin logged in")

        self.create_widgets()

    def create_widgets(self):
        self.bottom_frame.pack(side=ctk.RIGHT, anchor="ne", pady=(20, 0), padx=(0, 20))

        self.create_buttons()

        self.create_books_treeview()
        self.create_authors_treeview()

    def on_author_double_click(self, event):
        item_id = self.tv_authors.selection()[0]
        values = self.tv_authors.item(item_id, 'values')
        author_id = values[0]
        author_details = self.db.get_author_details(author_id)

        if author_details:
            AuthorDetail(self, author_details)
    def on_book_double_click(self, event):
        item_id = self.tv_books.selection()[0]
        values = self.tv_books.item(item_id, 'values')
        book_id = values[0]
        book_details = self.db.get_book_details(book_id)

        if book_details:
            BookDetail(self, book_details)

    def show_author_detail(self, author_id, author_name):

        book_list = self.db.get_books_by_author(author_id)

        detail_window = AuthorDetail(author_name, book_list)

        detail_window.mainloop()

    def show_book_detail(self, book_id, book_name, author_name):

        book_details = self.db.get_book_details(book_id)
        detail_window = BookDetail(book_name, author_name, book_details)
        detail_window.mainloop()

    def on_edit_book_click(self):

        selected_row_id = self.tv_books.selection()[0]
        selected_item_row = self.tv_books.item(selected_row_id)["values"]

        self.edit_book_page = edit_book.EditBook(parent=self, bid=int(selected_item_row[0])
                                                 , name=selected_item_row[1]
                                                 , author_name=selected_item_row[2], rowid=selected_row_id
                                                 )

    def on_edit_author_click(self):

        selected_row_id = self.tv_authors.selection()[0]
        selected_item_row = self.tv_authors.item(selected_row_id)["values"]

        self.edit_author_page = edit_author.EditAuthor(parent=self, aid=int(selected_item_row[0])
                                                       , name=selected_item_row[1], rowid=selected_row_id,
                                                       callback=self.update_books_treeview)

    def on_add_book_click(self):
        self.add_book_page = add_book.AddBook(parent=self, callback=self.update_books_treeview)

    def on_add_author_click(self):
        self.add_author_page = add_author.AddAuthor(parent=self, callback=self.update_authors_treeview)

    def on_delete_book_click(self):
        selected_row_id = self.tv_books.selection()[0]
        selected_item_row = self.tv_books.item(selected_row_id)["values"]
        selected_book_id = selected_item_row[0]
        selected_item = self.tv_books.selection()
        if selected_item:
            self.db.delete_book(int(selected_book_id))
            self.tv_books.delete(selected_item)

    def on_delete_author_click(self):
        selected_row_id = self.tv_authors.selection()[0]
        selected_item_row = self.tv_authors.item(selected_row_id)["values"]
        selected_author_id = selected_item_row[0]
        selected_item = self.tv_authors.selection()
        if selected_item:
            self.tv_authors.delete(selected_item)

            self.db.delete_author(int(selected_author_id))

            self.update_books_treeview()

    def on_search_button_click(self):
        self.search_page = search_page.SearchPage(self)

    def is_user(self):
        self.add_book_button.configure(state=ctk.DISABLED)
        self.edit_book_button.configure(state=ctk.DISABLED)
        self.delete_book_button.configure(state=ctk.DISABLED)

        self.add_author_button.configure(state=ctk.DISABLED)
        self.edit_author_button.configure(state=ctk.DISABLED)
        self.delete_author_button.configure(state=ctk.DISABLED)

    def create_buttons(self):
        self.add_book_button.grid(row=0, column=0, pady=(20, 0))
        self.edit_book_button.grid(row=0, column=1, pady=(20, 0))
        self.delete_book_button.grid(row=0, column=2, pady=(20, 0))

        self.add_author_button.grid(row=1, column=0, pady=(20, 0))
        self.edit_author_button.grid(row=1, column=1, pady=(20, 0))
        self.delete_author_button.grid(row=1, column=2, pady=(20, 0))

        self.search_button.grid(row=2, column=0, columnspan=3, pady=(20, 0))
        self.clear_database_button.grid(row=3, column=0, columnspan=3, pady=(20, 0))

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

    def update_books_treeview(self):
        # Clear the current items in the treeview
        for item in self.tv_books.get_children():
            self.tv_books.delete(item)

        # Reload data and insert updated items
        books_data = self.db.list_books()
        for data in books_data:
            self.tv_books.insert('', 'end', values=data)
            self.book_list.append(data)

    def update_authors_treeview(self):
        for item in self.tv_authors.get_children():
            self.tv_authors.delete(item)

        authors_data = self.db.list_authors()
        for data in authors_data:
            self.tv_authors.insert('', 'end', values=data)
            self.author_list.append(data)

    def clear_database(self):
        self.db.clear_database()
        self.update_authors_treeview()
        self.update_books_treeview()

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
