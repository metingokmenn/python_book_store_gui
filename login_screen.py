import tkinter as tk

from tkinter import ttk
import main_screen as ms

class LoginScreen:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("300x200")
        self.win.eval('tk::PlaceWindow . center')
        self.win.resizable(False, False)
        self.win.title('Login')

        self.win.bind("<Configure>", self.on_resize)

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.usernameLabel = None
        self.usernameEntry = None
        self.passwordLabel = None
        self.passwordEntry = None
        self.loginButton = None
        self.create_widgets()

    def create_widgets(self):
        self.usernameLabel = tk.Label(self.win, text="User Name")
        self.usernameLabel.grid(row=0, column=0, sticky="ew")
        self.usernameEntry = tk.Entry(self.win, textvariable=self.username, width=20)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel = tk.Label(self.win, text="Password")
        self.passwordLabel.grid(row=1, column=0, sticky="ew")
        self.passwordEntry = tk.Entry(self.win, textvariable=self.password, show='*')
        self.passwordEntry.grid(row=1, column=1)
        self.loginButton = tk.Button(self.win, text="Login", command=self.is_admin)
        self.loginButton.grid(row=4, column=0, columnspan=2, sticky="ew")

    def is_admin(self):
        if self.usernameEntry.get() == "admin" and self.passwordEntry.get() == "12345":
            self.navigate_to_main_screen()
            self.win.destroy()
        elif self.usernameEntry.get() == "user" and self.passwordEntry.get() == "67890":
            print("User has logged in.")
            self.navigate_to_main_screen()
        self.loginButton = tk.Button(self.win, text="Login", command=self.isAdmin)
        self.loginButton.grid(row=4, column=0, columnspan=2, sticky="ew")

            self.win.destroy()
        else:
            print("Invalid username")


    def on_resize(self, event):

        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        self.win.rowconfigure(0, weight=1)
        self.win.rowconfigure(1, weight=1)
        self.win.rowconfigure(2, weight=1)
        self.win.rowconfigure(3, weight=1)
        self.win.rowconfigure(4, weight=1)
        self.win.minsize(self.win.winfo_width(), self.win.winfo_height())


    def navigate_to_main_screen(self):
        self.win2 = ms.MainScreen(self)
        self.win2.grab_set()


=======
app = LoginScreen()
app.win.mainloop()
