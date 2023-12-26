import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class BookDetail:
    def __init__(self, parent, book_details):
        super().__init__()
        self.win = ctk.CTk()
        self.win.title("Book Detail")
        self.win.geometry("400x300")
        self.parent = parent
        self.book_details = book_details
        self.create_widgets()

    def create_widgets(self):
        print(self.book_details)

        try:
            book_id_label = ctk.CTkLabel(self.win, text=f"Book ID: {self.book_details[0]}")
            book_label = ctk.CTkLabel(self.win, text=f"Book Name: {self.book_details[1]}")
            author_label = ctk.CTkLabel(self.win, text=f"Author Name: {self.book_details[3]}")
            close_button = ctk.CTkButton(self.win, text="Close", command=self.close_window)

            book_id_label.pack(pady=5)
            book_label.pack(pady=5)
            author_label.pack(pady=5)
            close_button.pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def close_window(self):
        self.win.destroy()
