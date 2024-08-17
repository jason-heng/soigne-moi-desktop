from utils.ui import Colors, font_text, font_title
from utils.getters import *
from pages.components.patientsList import PatientsList
from utils.objects import Secretary

from customtkinter import *

class HomePage(CTkFrame):
    def __init__(self, window: CTk, token : str, secretary: Secretary, past_page: CTkFrame = None) -> None:
        if past_page:
            past_page.destroy()

        super().__init__(window, corner_radius=0, fg_color=Colors.TERTIARY)
        self.pack(fill="both", expand=True)
        self.window = window

        self.view()
    
    def view(self):
        PatientsList(self).pack()
