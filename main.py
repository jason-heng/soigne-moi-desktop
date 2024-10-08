from pages.login import LoginPage
from pages.home import HomePage
from utils.objects import Secretary
from utils.ui import Colors, center
from config import session_json_path

import customtkinter as ctk
from customtkinter import CTk
import json


class App(CTk):
    def __init__(self) -> None:
        super().__init__(fg_color=Colors.TERTIARY)
        self.title("SoigneMoi")

        self.resizable(False, False)
        center(1120, 620, self)

        try:
            with open(session_json_path, "r") as f:
                config = json.load(f)
                if config and config["token"]:
                    token: str = config["token"]
                    secretary = Secretary(config["secretary"])
                    HomePage(self, token, secretary)
                else:
                    LoginPage(self)
        except FileNotFoundError:
            LoginPage(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
