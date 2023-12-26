from tkinter import messagebox
import customtkinter as ctk


class AuthorDetail:
    def __init__(self, parent, author_details):
        super().__init__()
        self.win = ctk.CTk()
        self.win.title("Author Detail")
        self.win.geometry("400x300")
        self.parent = parent
        self.author_details = author_details
        self.create_widgets()

    def create_widgets(self):
        author_label = ctk.CTkLabel(self.win, text=f"Author Name: {self.author_details[0][1]}")
        author_label.pack(pady=10)

        try:
            if self.author_details[0][2] is not None:
                books_label = ctk.CTkLabel(self.win, text="Author's Books:")
                books_label.pack(pady=5)

                for book in self.author_details:
                    if book[2] is not None:
                        book_label = ctk.CTkLabel(self.win, text=f"Book ID: {book[2]}, Book Name: {book[3]}")
                        book_label.pack()

        except Exception as e:
            messagebox.showinfo("Error", f"Error occured: {str(e)}")

        close_button = ctk.CTkButton(self.win, text="Close", command=self.close_window)
        close_button.pack(pady=10)

    def close_window(self):
        self.win.destroy()
