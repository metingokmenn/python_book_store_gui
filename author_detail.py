from tkinter import messagebox
import customtkinter as ctk

import langpack


class AuthorDetail:
    def __init__(self, parent, author_details, language):
        super().__init__()
        self.win = ctk.CTk()
        self.win.title("Author Detail")
        self.win.geometry("400x300")
        self.parent = parent
        self.author_details = author_details
        self.language = language
        self.create_widgets()

    def create_widgets(self):
        self.reload_gui_text()
        author_label = ctk.CTkLabel(self.win, text=f"{self.i18n.authorname}: {self.author_details[0][1]}")
        author_label.pack(pady=10)

        try:
            if self.author_details[0][2] is not None:
                books_label = ctk.CTkLabel(self.win, text="Author's Books:")
                books_label.pack(pady=5)

                for book in self.author_details:
                    if book[2] is not None:
                        book_label = ctk.CTkLabel(self.win, text=f"{self.i18n.bookid}: {book[2]}, {self.i18n.bookname}: {book[3]}")
                        book_label.pack()

        except Exception as e:
            messagebox.showinfo(self.i18n.error, f"{self.i18n.errmessage}: {str(e)}")

        close_button = ctk.CTkButton(self.win, text="Close", command=self.close_window)
        close_button.pack(pady=10)



    #TO-DO
    def reload_gui_text(self):
        self.i18n = langpack.I18N(self.language)
        self.win.title(self.i18n.a)
        self.search_button.configure(text=self.i18n.search)
        self.search_label.configure(text=self.i18n.sptitle)

    def close_window(self):
        self.win.destroy()
