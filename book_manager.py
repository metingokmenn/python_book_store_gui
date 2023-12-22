from tkinter import messagebox, simpledialog
import tkinter as tk
from tkinter import ttk
from book import Book
import db

class BookManager:
    def __init__(self, win):
        self.win = win
        self.db = db.DatabaseManager()
        self.list_box = tk.Listbox(self.win, height=50, width=50, selectmode='SINGLE')
        self.book_labels = [
            ttk.Label(self.win, text=f"Book id: "),
            ttk.Label(self.win, text=f"Book name: "),
            ttk.Label(self.win, text=f"Author name: ")
        ]
        self.selected_item_index = None
        self.book_list = []

    def edit_book(self):
        try:
            if not self.selected_item_index:
                raise ValueError("Please select a book to edit.")

            selected_book = self.book_list[self.selected_item_index[0]]
            new_book_name = simpledialog.askstring("Edit Book",
                                                   f"Enter the new book name for ID {selected_book.id}:")
            new_author_name = simpledialog.askstring("Edit Book",
                                                     f"Enter the new author name for ID {selected_book.id}:")

            if new_book_name and new_author_name is not None:
                selected_book.name = new_book_name
                selected_book.author = new_author_name
                updated_text = str(selected_book)
                self.list_box.delete(self.selected_item_index[0])
                self.list_box.insert(self.selected_item_index[0], updated_text)

        except Exception as e:
            messagebox.showwarning("Edit Book", f"Error editing book: {str(e)}")

        else:
            messagebox.showinfo("Edit Book", "Book successfully edited.")


    def list_maker(self):
        for i in range(50):
            book_info = Book(i + 1, f"Book Label", f"Author")
            self.book_list.append(book_info)
            display_text = str(book_info)
            self.list_box.insert(tk.END, display_text)

    def on_item_select(self, event):
        self.selected_item_index = self.list_box.curselection()

        if self.selected_item_index:
            selected_book = self.book_list[self.selected_item_index[0]]

            self.book_labels[0].configure(text=f"Book id: {selected_book.id}")
            self.book_labels[1].configure(text=f"Book name: {selected_book.name}")

            self.book_labels[2].configure(text=f"Author name: {selected_book.author}")

    def add_book(self):
        try:
            book_name = simpledialog.askstring("Add Book", "Enter the book name:")
            author_name = simpledialog.askstring("Add Book", "Enter the author name:")

            if book_name and author_name is not None:
                book_info = Book(len(self.book_list) + 1, book_name, author_name)
                self.book_list.append(book_info)
                display_text = str(book_info)
                self.list_box.insert(tk.END, display_text)

        except Exception as e:
            messagebox.showwarning("Add Book", f"Error adding book: {str(e)}")

        else:
            messagebox.showinfo("Add Book", "Book successfully added.")
