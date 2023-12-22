import tkinter as tk
from tkinter import ttk

from full_screen import full_screen

<<<<<<< Updated upstream
=======
import db


>>>>>>> Stashed changes
class MainScreen(tk.Toplevel):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
<<<<<<< Updated upstream
=======
        self.db = db.DatabaseManager()
>>>>>>> Stashed changes
        self.win = tk.Tk()
        self.win.title('Main Screen')
        self.win.geometry(full_screen(self.win))
        self.win.resizable(True, True)
        self.labels = []
        self.list_box = tk.Listbox(self.win, height=self.win.winfo_screenheight(), selectmode='SINGLE')
        self.bottom_frame = tk.Frame(self.win)
        self.book_id_label = ttk.Label(self.bottom_frame, text=f"Book id: ")
        self.book_name_label = ttk.Label(self.bottom_frame, text=f"Book name: ")
        self.author_name_label = ttk.Label(self.bottom_frame, text=f"Author name: ")
        self.list_box.bind("<ButtonRelease-1>", self.onItemSelect)
        self.addButton = None
        self.deleteButton = None
        if(parent.usernameEntry.get() == "user"):
            print("User logged")
        elif():
            print("Admin logged")      
        self.create_widgets()

<<<<<<< Updated upstream
    def listMaker(self):
        for i in range(50):
            self.label_text = f"Label {i}"
=======
    def edit_book(self):
        print(self.db.list_books)

    def edit_author(self):
        if not self.selected_item_index_author:
            messagebox.showinfo("Edit Author", "Please select a author to edit.")
            return

        selected_item_index = self.selected_item_index_author[0]
        selected_author = self.author_list[selected_item_index]

        new_author_name = simpledialog.askstring("Edit Author",
                                                 f"Enter the new author name for ID {selected_author.id}:",
                                                 parent=self.win)
        new_author_books = []

        if new_author_name is not None:
            selected_author.name = new_author_name
            selected_author.books = new_author_books

            updated_text = f"Author: {selected_author.name} - Books: {selected_author.books} - ID: {selected_author.id}"
            self.list_box_author.delete(selected_item_index)
            self.list_box_author.insert(selected_item_index, updated_text)

            # Güncelleme sonrasında seçilen öğeyi güncelle
            self.on_item_select_author(None)

    def update_book_ids_after_delete(self, deleted_index):
        # Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.parent.book_list)):
            self.parent.book_list[i].id = i + 1

    def update_author_ids_after_delete(self, deleted_index):
        # Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.author_list)):
            self.author_list[i].id = i + 1

    def delete_book(self):
        if not self.selected_item_index_book:
            messagebox.showinfo("Error", "Please select a book to delete.")
            return

        deleted_index = self.selected_item_index_book[0]
        self.list_box_book.delete(deleted_index)
        deleted_book = self.book_list.pop(deleted_index)
        self.update_book_ids_after_delete(deleted_index)
        self.selected_item_index_book = None

        if self.selected_item_index_book:
            messagebox.showinfo("Success", f"Book '{deleted_book.name}' deleted successfully.")

        # Güncelleme: Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.book_list)):
            self.book_list[i].id = i + 1

    def delete_author(self):
        if not self.selected_item_index_author:
            messagebox.showinfo("Error", "Please select a author to delete.")
            return

        deleted_index = self.selected_item_index_author[0]
        self.list_box_author.delete(deleted_index)
        deleted_author = self.author_list.pop(deleted_index)
        self.update_author_ids_after_delete(deleted_index)
        self.selected_item_index_author = None

        if self.selected_item_index_author:
            messagebox.showinfo("Success", f"Book '{deleted_author.name}' deleted successfully.")

        # Güncelleme: Silinen öğeden sonraki tüm öğelerin ID'lerini güncelle
        for i in range(deleted_index, len(self.author_list)):
            self.author_list[i].id = i + 1

    def list_maker_book(self):
        for i in range(50):
            book_info = Book(i + 1, f"Book Label", f"Author")
            self.book_list.append(book_info)
            display_text = f"{book_info.name} - {book_info.author} - ID: {book_info.id}"
            self.list_box_book.insert(tk.END, self.db.list_books)
>>>>>>> Stashed changes

            self.labels.append(self.label_text)
            self.list_box.insert(i, self.labels[i])

    def create_widgets(self):
        self.bottom_frame.pack(side=tk.RIGHT, anchor="ne", pady=(20, 0), padx=(0, 20))
        self.book_id_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.book_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.author_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
        self.list_box.pack(pady=(20, 0), padx=(20, 0), anchor="nw")
        self.listMaker() 

    def onItemSelect(self, event):
        self.selected_item_index = self.list_box.curselection()

        if(self.selected_item_index):
            self.selected_item = self.list_box.get(self.selected_item_index[0])

        self.book_name_label.configure(text=f"Book name: {self.selected_item}")
        self.book_id_label.configure(text=f"Book id: {self.selected_item_index[0]}")
        #TO-DO author label    
