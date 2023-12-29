
import customtkinter as ctk
import langpack
import db


class SearchPage:
    def __init__(self, parent, language):
        super().__init__()
        self.parent = parent

        self.win = ctk.CTk()
        self.win.title("Search Page")
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)
        self.win.geometry("765x450+710+150")

        self.db = db.DatabaseManager()
        self.language = language
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
        self.reload_gui_text()

    def reload_gui_text(self):
        self.i18n = langpack.I18N(self.language)
        self.win.title(self.i18n.sptitle)
        self.search_button.configure(text=self.i18n.search)
        self.search_label.configure(text=self.i18n.sptitle)

    def on_search(self):
        self.searched_list = self.db.search(self.search_key.get())
        self.search_result_label_text = ''
        print(self.searched_list)
        for item in self.searched_list:

            if item is not None:
                if len(item) == 2:
                    self.search_result_label_text += f"{self.i18n.authorid}: {item[0]}, {self.i18n.authorname}: {item[1]}\n"
                if len(item) == 3:
                    author_name = self.db.get_authorname_by_aid(item[2])
                    self.search_result_label_text += f"{self.i18n.bookid}: {item[0]}, {self.i18n.bookname}: {item[1]}, {self.i18n.authorname}: {author_name}\n"

        self.search_result_label.configure(text=self.search_result_label_text)


    def close_window(self):
        self.win.destroy()

