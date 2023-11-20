import tkinter as tk
from tkinter import ttk

from full_screen import full_screen

class MainScreen(tk.Toplevel):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
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

    def listMaker(self):
        for i in range(50):
            self.label_text = f"Label {i}"

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
