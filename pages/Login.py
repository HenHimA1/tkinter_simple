import tkinter
from database import AppDatabase


class LoginPage(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.email_val = tkinter.StringVar(value="")
        self.pass_val = tkinter.StringVar(value="")

        tkinter.Label(master=self, text="Email").pack()
        tkinter.Entry(master=self, textvariable=self.email_val).pack()
        tkinter.Label(master=self, text="Password").pack()
        tkinter.Entry(master=self, show="*", textvariable=self.pass_val).pack()
        tkinter.Button(self, text="Login", command=self.click_login).pack()

    def click_login(self):
        domain = [("email", "=", self.email_val.get()),
                  ("password", "=", self.pass_val.get())]
        records = AppDatabase().select_record("USER", domain)
        if records:
            self.controller.show_frame("MainPage")
