from utils.ui import font_title, font_text, center_x
from utils.ui import Colors

from customtkinter import *

class LoginPage(CTkFrame):
    def __init__(self, window: CTk, past_page: CTkFrame = None) -> None:
        if past_page:
            past_page.destroy()

        super().__init__(window, corner_radius=0, fg_color=Colors.PRIMARY)
        self.pack(fill="both", expand=True)
        self.window = window
        
        self.view()

    def view(self):
        logo_text = CTkLabel(self, text="SoigneMoi", font=font_title(48), text_color=Colors.TERTIARY)
        print(center_x(logo_text, self, self))
        logo_text.place(x=center_x(logo_text, self, self), y=65)