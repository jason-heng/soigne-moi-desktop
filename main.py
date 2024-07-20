from pages.login import LoginPage
from pages.home import HomePage
from utils.ui import Colors, center

import customtkinter as ctk
from customtkinter import CTk
import json

class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color=Colors.TERTIARY)
        self.title("SoigneMoi")

        self.minsize(width=800, height=675)
        self.maxsize(width=1280, height=720)
        center(1120, 620, self)

        LoginPage(self)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
