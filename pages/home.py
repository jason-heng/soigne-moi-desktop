from customtkinter import *
from utils.ui import Colors


class HomePage(CTkFrame):
    def __init__(self, window: CTk, past_page: CTkFrame = None) -> None:
        if past_page:
            past_page.destroy()

        super().__init__(window, corner_radius=0, fg_color=Colors.TERTIARY)
        self.pack(fill="both", expand=True)

        self.window = window
