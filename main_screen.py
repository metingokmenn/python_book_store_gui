import tkinter as tk
from tkinter import ttk

from full_screen import full_screen


def on_item_select(event):
    selected_item_index = list_box.curselection()
    if(selected_item_index):
        selected_item = list_box.get(selected_item_index[0])

        book_name_label.configure(text=f"Book name: {selected_item}")
        book_id_label.configure(text=f"Book id: {selected_item_index[0]}")
        #TO-DO author label



win = tk.Tk()
win.title('Main Screen')
win.geometry(full_screen(win))
win.resizable(True, True)

labels = []
list_box = tk.Listbox(win, height=win.winfo_screenheight(), selectmode='SINGLE')
for i in range(50):
    label_text = f"Label {i}"

    labels.append(label_text)
    list_box.insert(i, labels[i])

bottom_frame = tk.Frame(win)
bottom_frame.pack(side=tk.RIGHT, anchor="ne", pady=(20, 0), padx=(0, 20))

book_id_label = ttk.Label(bottom_frame, text=f"Book id: ")
book_name_label = ttk.Label(bottom_frame, text=f"Book name: ")
author_name_label = ttk.Label(bottom_frame, text=f"Author name: ")

book_id_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
book_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")
author_name_label.pack(padx=(0, 500), pady=(20, 0), anchor="nw")

list_box.pack(pady=(20, 0), padx=(20, 0), anchor="nw")

list_box.bind("<ButtonRelease-1>", on_item_select)


win.mainloop()
