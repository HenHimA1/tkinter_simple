from pages import Login, Main
from database import AppDatabase
import tkinter

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        AppDatabase().execute(
            query="CREATE TABLE IF NOT EXISTS USER (id INTEGER NOT NULL PRIMARY KEY, email CHAR, password CHAR);")
        AppDatabase().execute(
            query="INSERT OR IGNORE INTO USER(id, email, password) VALUES(1, 'admin@mail.com', 'admin')")

        self.title("Simple APP")
        self.geometry("800x600")

        container = tkinter.Frame(self)
        container.pack(expand=True)
        
        self.frames = {}
        for F in [Login.LoginPage, Main.MainPage]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("LoginPage")

        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
