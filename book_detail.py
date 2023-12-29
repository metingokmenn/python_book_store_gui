import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

import langpack


class BookDetail:
    def __init__(self, parent, book_details, language):
        super().__init__()
        self.win = ctk.CTk()
        self.win.title("Book Detail")
        self.win.geometry("400x300")
        self.parent = parent
        self.book_details = book_details
        self.language = language
        self.create_widgets()


    def create_widgets(self):
        print(self.book_details)
        self.reload_gui_text()
        try:
            self.book_id_label = ctk.CTkLabel(self.win, text=f"{self.i18n.bookid}: {self.book_details[0]}")
            self.book_label = ctk.CTkLabel(self.win, text=f"{self.i18n.bookname}: {self.book_details[1]}")
            self.author_label = ctk.CTkLabel(self.win, text=f"{self.i18n.authorname}: {self.book_details[3]}")
            self.close_button = ctk.CTkButton(self.win, text="Close", command=self.close_window)

            self.book_id_label.pack(pady=5)
            self.book_label.pack(pady=5)
            self.author_label.pack(pady=5)
            self.close_button.pack(pady=10)

        except Exception as e:
            messagebox.showerror(self.i18n.error, f"{self.i18n.errmessage}: {str(e)}")



    def reload_gui_text(self):
        self.i18n = langpack.I18N(self.language)
        self.win.title(self.i18n.sptitle)

    def close_window(self):
        self.win.destroy()
