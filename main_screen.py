
from tkinter import simpledialog, messagebox
import tkinter as tk
from tkinter import ttk

from author import Author
from book import Book
from full_screen import full_screen



class MainScreen(tk.Toplevel):
    def __init__(self, parent):

        super().__init__()

        self.parent = parent


        self.win = tk.Tk()
        self.win.title('Main Screen')
        self.win.geometry(full_screen(self.win))
        self.win.resizable(True, True)

        self.book_list = []  # Her bir kitap öğesini içeren liste
        self.author_list = []
        self.list_box_book = tk.Listbox(self.win, height=50, width=50, selectmode='SINGLE')
        self.list_box_author = tk.Listbox(self.win, height=50, width=50, selectmode='SINGLE')
        self.bottom_frame = tk.Frame(self.win)
        self.book_id_label = ttk.Label(self.bottom_frame, text=f"Book id: ", font=("Times", "16", "bold"))
        self.book_name_label = ttk.Label(self.bottom_frame, text=f"Book name: ", font=("Times", "16", "bold"))
        self.author_name_label = ttk.Label(self.bottom_frame, text=f"Author name: ", font=("Times", "16", "bold"))
        self.list_box_book.bind("<ButtonRelease-1>", self.on_item_select_book)
        self.list_box_author.bind("<ButtonRelease-1>", self.on_item_select_author)
        self.selected_item_index_book = None
        self.selected_item_index_author = None


        if parent.usernameEntry.get() == "user":
            print("user logged in")
        elif parent.usernameEntry.get() == "admin":
            print("admin logged in")

        self.create_widgets()

    def edit_book(self):
        if not self.selected_item_index_book:
            messagebox.showinfo("Edit Book", "Please select a book to edit.")
            return

        selected_item_index = self.selected_item_index_book[0]
        selected_book = self.book_list[selected_item_index]



        new_book_name = simpledialog.askstring("Edit Book",
                                               f"Enter the new book name for ID {selected_book.id}:", parent=self.win)
        new_author_name = simpledialog.askstring("Edit Book",
                                                 f"Enter the new author name for ID {selected_book.id}:", parent=self.win)

        if new_book_name and new_author_name is not None:
            selected_book.name = new_book_name
            selected_book.author = new_author_name

            updated_text = f"Book: {selected_book.name} - Author: {selected_book.author} - ID: {selected_book.id}"
            self.list_box_book.delete(selected_item_index)
            self.list_box_book.insert(selected_item_index, updated_text)

            # Güncelleme sonrasında seçilen öğeyi güncelle
            self.on_item_select_book(None)

    def update_book_ids_after_delete(self, deleted_index):
        # Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.parent.book_list)):
            self.parent.book_list[i].id = i + 1

    def delete_book(self):
        if not self.selected_item_index_book:
            messagebox.showinfo("Error", "Please select a book to delete.")
            return

        deleted_index = self.selected_item_index_book[0]
        self.list_box_book.delete(deleted_index)
        deleted_book = self.book_list.pop(deleted_index)
        self.update_book_ids_after_delete(deleted_index)
        self.selected_item_index_book = None

        if  self.selected_item_index_book:
            messagebox.showinfo("Success", f"Book '{deleted_book.name}' deleted successfully.")

        # Güncelleme: Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.book_list)):
            self.book_list[i].id = i + 1

    def list_maker_book(self):
        for i in range(50):
            book_info = Book(i + 1, f"Book Label", f"Author")
            self.book_list.append(book_info)
            display_text = f"{book_info.name} - {book_info.author} - ID: {book_info.id}"
            self.list_box_book.insert(tk.END, display_text)

    def list_maker_author(self):
        for i in range(50):
            author_info = Author(i + 1, f"Author Name", f"Author Books")
            self.author_list.append(author_info)
            display_text = f"{author_info.name} - {author_info.books} - ID: {author_info.id}"
            self.list_box_author.insert(tk.END, display_text)

    def create_widgets(self):
        self.bottom_frame.pack(side=tk.RIGHT, anchor="ne", pady=(20, 0), padx=(0, 20))
        self.book_id_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.book_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.author_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.list_box_book.pack(pady=(20, 0), padx=(20, 0), anchor="nw", side=tk.LEFT)
        self.list_box_author.pack(pady=(20,0),padx=(40, 0), side=tk.LEFT, anchor="nw")



        if self.parent.usernameEntry.get() == "admin":
            self.add_book_button = tk.Button(self.bottom_frame, text="Add Book", command=self.add_book)
            self.add_book_button.pack(side=tk.LEFT, pady=(20, 0))
            self.edit_book_button = tk.Button(self.bottom_frame, text="Edit Book", command=self.edit_book)
            self.edit_book_button.pack(side=tk.LEFT, pady=(20, 0))

            self.delete_book_button = tk.Button(self.bottom_frame, text="Delete Book", command=self.delete_book)
            self.delete_book_button.pack(side=tk.LEFT, pady=(20, 0))

            self.add_author_button = tk.Button(self.bottom_frame, text="Add Author", command=self.add_book)
            self.add_author_button.pack( side=tk.LEFT, padx=(40, 0), pady=(20, 0))
            self.edit_author_button = tk.Button(self.bottom_frame, text="Edit Author", command=self.edit_book)
            self.edit_author_button.pack(side=tk.LEFT, pady=(20, 0))

            self.delete_author_button = tk.Button(self.bottom_frame, text="Delete Author", command=self.delete_book)
            self.delete_author_button.pack(side=tk.LEFT, pady=(20, 0))

        else:
            self.add_book_button = tk.Button(self.bottom_frame, text="Add Book", state=tk.DISABLED)
            self.add_book_button.pack(side=tk.TOP)
            self.edit_book_button = tk.Button(self.bottom_frame, text="Edit Book", state=tk.DISABLED)
            self.edit_book_button.pack(side=tk.TOP)
            self.delete_book_button = tk.Button(self.bottom_frame, text="Delete Book", state=tk.DISABLED)
            self.delete_book_button.pack(side=tk.TOP)

        self.list_maker_book()
        self.list_maker_author()

    def on_item_select_book(self, event):
        self.selected_item_index_book = self.list_box_book.curselection()

        if self.selected_item_index_book:
            selected_item_info = self.book_list[self.selected_item_index_book[0]]

            self.book_name_label.configure(text=f"Book name: {selected_item_info.name}")
            self.book_id_label.configure(text=f"Book ID: {selected_item_info.id}")
            self.author_name_label.configure(text=f"Author name: {selected_item_info.author}")

            self.edit_book_button.configure(state=tk.ACTIVE)
            self.add_book_button.configure(state=tk.ACTIVE)
            self.delete_book_button.configure(state=tk.ACTIVE)

            self.edit_author_button.configure(state=tk.DISABLED)
            self.add_author_button.configure(state=tk.DISABLED)
            self.delete_author_button.configure(state=tk.DISABLED)

    def on_item_select_author(self, event):
        self.selected_item_index_author = self.list_box_author.curselection()

        if self.selected_item_index_author:
            selected_item_info = self.author_list[self.selected_item_index_author[0]]

            self.book_name_label.configure(text=f"Author name: {selected_item_info.name}")
            self.book_id_label.configure(text=f"Author ID: {selected_item_info.id}")
            self.author_name_label.configure(text=f"Author books: {selected_item_info.books}")

            self.edit_book_button.configure(state=tk.DISABLED)
            self.add_book_button.configure(state=tk.DISABLED)
            self.delete_book_button.configure(state=tk.DISABLED)

            self.edit_author_button.configure(state=tk.ACTIVE)
            self.add_author_button.configure(state=tk.ACTIVE)
            self.delete_author_button.configure(state=tk.ACTIVE)

    def add_book(self):
        book_name = simpledialog.askstring("Add Book", "Enter the book name:", parent=self.win)
        author_name = simpledialog.askstring("Add Book", "Enter the author name:", parent=self.win)

        if book_name and author_name is not None:
            max_id = max(book.id for book in self.book_list) if self.book_list else 0
            new_book_id = max_id + 1
            book_info = Book(new_book_id, book_name, author_name)
            self.book_list.append(book_info)
            display_text = f"Book: {book_info.name} - Author: {book_info.author} - ID: {book_info.id}"
            self.list_box_book.insert(tk.END, display_text)


    def add_author(self):
        author_name = simpledialog.askstring("Add Author", "Enter the author name:", parent=self.win)
        author_books = []

        if author_name is not None:
            max_id = max(book.id for book in self.author_list) if self.author_list else 0
            new_author_id = max_id + 1
            author_info = Author(new_author_id,author_name,author_books)
            self.author_list.append(author_info)
            display_text = author_info.__str__()

