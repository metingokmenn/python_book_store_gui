import tkinter as tk
import customtkinter as ctk

import db


class SearchPage:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.win = ctk.CTk()
        self.win.title("Search Page")
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)
        self.win.geometry("765x450+710+150")

        self.db = db.DatabaseManager()
        self.searched_list = []
        self.search_result_label_text = ''
        self.search_key = ctk.StringVar()
        self.search_label = ctk.CTkLabel(self.win, text="Search: ")
        self.search_entry = ctk.CTkEntry(self.win, textvariable=self.search_key)
        self.search_button = ctk.CTkButton(self.win, text='Search', command=self.on_search)

        self.search_result_label = ctk.CTkLabel(self.win, text=self.search_result_label_text)

        self.create_widgets()

    def create_widgets(self):
        self.search_label.pack()
        self.search_entry.pack(pady=(30, 30))
        self.search_button.pack()
        self.search_result_label.pack(pady=(30, 0))

    def on_search(self):
        self.searched_list = self.db.search(self.search_key.get())
        self.search_result_label_text = ''
        print(self.searched_list)
        for item in self.searched_list:

            if item is not None:
                if len(item) == 2:
                    self.search_result_label_text += f"Author ID: {item[0]}, Author name: {item[1]}\n"
                if len(item) == 3:
                    author_name = self.db.get_authorname_by_aid(item[2])
                    self.search_result_label_text += f"Book ID: {item[0]}, Book name: {item[1]}, Author name: {author_name}\n"

        self.search_result_label.configure(text=self.search_result_label_text)




    def close_window(self):
        self.win.destroy()

