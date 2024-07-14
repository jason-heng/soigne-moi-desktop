from pages.login import LoginPage
from pages.home import HomePage
from utils.ui import Colors

import customtkinter as ctk
from customtkinter import CTk
import json

class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color=Colors.TERTIARY)
        self.title("SoigneMoi")

        self.geometry("1280x720")
        self.resizable(False, False)

        LoginPage(self)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
