from utils.ui import Colors, font_text, font_title, focus_event
from utils.getters import *
from pages.components.patientsList import PatientsList
from pages.components.dashboard import HomeDashboard
from utils.objects import Secretary

from customtkinter import *

class HomePage(CTkFrame):
    def __init__(self, window: CTk, token : str, secretary: Secretary, past_page: CTkFrame = None) -> None:
        if past_page:
            past_page.destroy()

        super().__init__(window, corner_radius=0, fg_color=Colors.TERTIARY)
        self.pack(fill="both", expand=True)
        self.window = window
        self.token = token
        self.secretary = secretary

        self.view()
        focus_event(self.window)
    
    def view(self):
        PatientsList(self, self.token).place(relheight=1, relwidth=0.3, x=0, y=0)

        page_content = CTkFrame(self, fg_color=Colors.TERTIARY, width=770, corner_radius=0)
        page_content.pack(fill="y", side=RIGHT)

        title = CTkLabel(page_content, text="Informations du jour", font=font_title(22), text_color=Colors.SECONDARY)
        title.place(relx=0.5, y=50, anchor=CENTER)

        home_dashboad = HomeDashboard(page_content, self.token)
        home_dashboad.place(x=0, y=88)
