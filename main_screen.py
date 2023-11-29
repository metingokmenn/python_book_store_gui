from tkinter import simpledialog, messagebox
import tkinter as tk
from tkinter import ttk
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
        self.list_box = tk.Listbox(self.win, height=50, width=50, selectmode='SINGLE')
        self.bottom_frame = tk.Frame(self.win)
        self.book_id_label = ttk.Label(self.bottom_frame, text=f"Book id: ", font=("Times", "16", "bold"))
        self.book_name_label = ttk.Label(self.bottom_frame, text=f"Book name: ", font=("Times", "16", "bold"))
        self.author_name_label = ttk.Label(self.bottom_frame, text=f"Author name: ", font=("Times", "16", "bold"))
        self.list_box.bind("<ButtonRelease-1>", self.on_item_select)
        self.selected_item_index = None

        if parent.usernameEntry.get() == "user":
            print("user logged in")
        elif parent.usernameEntry.get() == "admin":
            print("admin logged in")

        self.create_widgets()

    def edit_book(self):
        if not self.selected_item_index:
            messagebox.showinfo("Edit Book", "Please select a book to edit.")
            return

        selected_item_index = self.selected_item_index[0]
        selected_book = self.book_list[selected_item_index]

        new_book_name = simpledialog.askstring("Edit Book",
                                               f"Enter the new book name for ID {selected_book.id}:")
        new_author_name = simpledialog.askstring("Edit Book",
                                                 f"Enter the new author name for ID {selected_book.id}:")

        if new_book_name and new_author_name is not None:
            selected_book.name = new_book_name
            selected_book.author = new_author_name

            updated_text = f"Book: {selected_book.name} - Author: {selected_book.author} - ID: {selected_book.id}"
            self.list_box.delete(selected_item_index)
            self.list_box.insert(selected_item_index, updated_text)

            # Güncelleme sonrasında seçilen öğeyi güncelle
            self.on_item_select(None)

    def update_book_ids_after_delete(self, deleted_index):
        # Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.parent.book_list)):
            self.parent.book_list[i].id = i + 1

    def delete_book(self):
        if not self.selected_item_index:
            messagebox.showinfo("Error", "Please select a book to delete.")
            return

        deleted_index = self.selected_item_index[0]
        self.list_box.delete(deleted_index)
        deleted_book = self.book_list.pop(deleted_index)
        self.update_book_ids_after_delete(deleted_index)
        self.selected_item_index = None

        if  self.selected_item_index:
            messagebox.showinfo("Success", f"Book '{deleted_book.name}' deleted successfully.")

        # Güncelleme: Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.book_list)):
            self.book_list[i].id = i + 1

    def list_maker(self):
        for i in range(50):
            book_info = Book(i + 1, f"Book Label", f"Author")
            self.book_list.append(book_info)
            display_text = f"{book_info.name} - {book_info.author} - ID: {book_info.id}"
            self.list_box.insert(tk.END, display_text)

    def create_widgets(self):
        self.bottom_frame.pack(side=tk.RIGHT, anchor="ne", pady=(20, 0), padx=(0, 20))
        self.book_id_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.book_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.author_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.list_box.pack(pady=(20, 0), padx=(20, 0), anchor="nw")

        if self.parent.usernameEntry.get() == "admin":
            self.add_book_button = tk.Button(self.bottom_frame, text="Add Book", command=self.add_book)
            self.add_book_button.pack(side=tk.TOP)
            self.edit_book_button = tk.Button(self.bottom_frame, text="Edit Book", command=self.edit_book)
            self.edit_book_button.pack(side=tk.TOP)

            self.delete_book_button = tk.Button(self.bottom_frame, text="Delete Book", command=self.delete_book)
            self.delete_book_button.pack(side=tk.TOP)
        else:
            self.add_book_button = tk.Button(self.bottom_frame, text="Add Book", state=tk.DISABLED)
            self.add_book_button.pack(side=tk.TOP)
            self.edit_book_button = tk.Button(self.bottom_frame, text="Edit Book", state=tk.DISABLED)
            self.edit_book_button.pack(side=tk.TOP)
            self.delete_book_button = tk.Button(self.bottom_frame, text="Delete Book", state=tk.DISABLED)
            self.delete_book_button.pack(side=tk.TOP)

        self.list_maker()

    def on_item_select(self, event):
        self.selected_item_index = self.list_box.curselection()

        if self.selected_item_index:
            selected_item_info = self.book_list[self.selected_item_index[0]]

            self.book_name_label.configure(text=f"Book name: {selected_item_info.name}")
            self.book_id_label.configure(text=f"Book ID: {selected_item_info.id}")
            self.author_name_label.configure(text=f"Author name: {selected_item_info.author}")

    def add_book(self):
        book_name = simpledialog.askstring("Add Book", "Enter the book name:")
        author_name = simpledialog.askstring("Add Book", "Enter the author name:")

        if book_name and author_name is not None:
            max_id = max(book.id for book in self.book_list) if self.book_list else 0
            new_book_id = max_id + 1
            book_info = Book(new_book_id, book_name, author_name)
            self.book_list.append(book_info)
            display_text = f"Book: {book_info.name} - Author: {book_info.author} - ID: {book_info.id}"
            self.list_box.insert(tk.END, display_text)
