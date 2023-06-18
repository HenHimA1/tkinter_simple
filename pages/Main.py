import tkinter

class MainPage(tkinter.Frame):
    def __init__(self, parent, controller):
        super(MainPage, self).__init__(parent)
        self.controller = controller
        self.email_val = tkinter.StringVar(value="")
        self.pass_val = tkinter.StringVar(value="")

        tkinter.Label(master=self, text="Welcome").pack()