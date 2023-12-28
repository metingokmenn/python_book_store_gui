import customtkinter as ctk
import main_screen as ms
import tkinter as tk
import langpack
from tkinter import messagebox as msg


class LoginScreen:
    def __init__(self):
        self.win = ctk.CTk()
        self.win.geometry("300x200")
        self.win.eval('tk::PlaceWindow . center')
        ctk.set_appearance_mode("dark")
        self.win.resizable(False, False)
        self.win.title('Login')

        self.bind_widgets()
        self.selected_language = tk.StringVar(value="en")
        self.i18n = langpack.I18N(self.selected_language.get())

        self.usernameLabel = None
        self.usernameEntry = None
        self.passwordLabel = None
        self.passwordEntry = None
        self.loginButton = None
        self.create_widgets()

    def create_widgets(self):

        self.usernameLabel = ctk.CTkLabel(self.win, text="User Name")
        self.usernameLabel.grid(row=0, column=0, sticky="ew")
        self.usernameEntry = ctk.CTkEntry(self.win)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel = ctk.CTkLabel(self.win, text="Password")
        self.passwordLabel.grid(row=1, column=0, sticky="ew")
        self.passwordEntry = ctk.CTkEntry(self.win, show='*')
        self.passwordEntry.grid(row=1, column=1)

        self.loginButton = ctk.CTkButton(self.win, text="Login")
        self.loginButton.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.usernameEntry.focus_set()

        self.loginButton.bind("<Button-1>", self.is_admin)
        self.win.bind("<Configure>", self.on_resize)
        self.passwordEntry.bind("<Return>", self.is_admin)

        self.context_menu = tk.Menu(self.win, tearoff=False)
        self.context_menu.add_radiobutton(label="English", variable=self.selected_language, value="en",
                                          command=lambda: self.reload_gui_text("en"))
        self.context_menu.add_radiobutton(label="Türkçe", variable=self.selected_language, value="tr",
                                          command=lambda: self.reload_gui_text("tr"))

    def reload_gui_text(self,language):
        self.i18n = langpack.I18N(language)
        self.win.title(self.i18n.logintitle)
        self.usernameLabel.configure(text=self.i18n.username)
        self.passwordLabel.configure(text=self.i18n.password)
        self.loginButton.configure(text=self.i18n.login)


    def bind_widgets(self):
        self.win.bind("<Button-2>", self.show_context_menu)

    def show_context_menu(self,event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def is_admin(self, event):

        if self.usernameEntry.get() == "admin" and self.passwordEntry.get() == "12345":
            self.navigate_to_main_screen()

        elif self.usernameEntry.get() == "user" and self.passwordEntry.get() == "67890":
            print("User has logged in.")
            self.navigate_to_main_screen()

        else:
            print("Invalid username")
            msg.showinfo(title='Invalid credentials !', message='Invalid username or password !')

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

        self.win.destroy()


app = LoginScreen()
app.win.mainloop()
