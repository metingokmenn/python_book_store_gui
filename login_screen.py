import tkinter as tk

def on_resize(event):
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    win.rowconfigure(3, weight=1)
    win.rowconfigure(4, weight=1)

def isAdmin():
    if(usernameEntry.get() == "admin" and passwordEntry.get() == "12345"):
        print("Admin has logged in.")
        win.destroy()
    elif(usernameEntry.get() == "user" and passwordEntry.get() == "67890"):
        print("User has logged in.") 
        win.destroy()
    else:
        print("Invalid username")          

win = tk.Tk()
win.geometry("300x200")
win.eval('tk::PlaceWindow . center')
win.resizable(False,False)
win.title('Login')

win.bind("<Configure>", on_resize)

usernameLabel = tk.Label(win, text="User Name")
usernameLabel.grid(row=0, column=0, sticky="ew")
username = tk.StringVar()
usernameEntry = tk.Entry(win, textvariable=username, width=20)
usernameEntry.grid(row=0, column=1)

passwordLabel = tk.Label(win, text="Password")
passwordLabel.grid(row=1, column=0, sticky="ew")
password = tk.StringVar()
passwordEntry = tk.Entry(win, textvariable=password, show='*')
passwordEntry.grid(row=1, column=1)

loginButton = tk.Button(win, text="Login", command=isAdmin)
loginButton.grid(row=4, column=0, columnspan=2, sticky="ew")

win.update_idletasks()
win.minsize(win.winfo_width(), win.winfo_height())

win.mainloop()
