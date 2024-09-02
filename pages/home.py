from utils.ui import Colors, font_text, font_title, focus_event
from utils.getters import *
from pages.components.patientsList import PatientsList
from pages.components.dashboard import HomeDashboard
from utils.objects import Secretary
from pages import login

from customtkinter import *


class PageContent(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Colors.TERTIARY, width=770, corner_radius=0)
        self.placed_item : CTkFrame | None = None



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

        self.page_content = PageContent(self)
        self.page_content.pack(fill="y", side=RIGHT)

        title = CTkLabel(self.page_content, text="Informations du jour", font=font_title(22), text_color=Colors.SECONDARY)
        title.place(x=5, y=30)

        self.home_dashboad = HomeDashboard(self.page_content, self.token)
        self.home_dashboad.place(x=0, y=88)
        self.page_content.placed_item = self.home_dashboad

        refresh_button = CTkButton(
            self.page_content,
            width=120,
            height=30,
            fg_color=Colors.PRIMARY,
            text="Rafraîchir",
            font=font_title(16),
            text_color=Colors.WHITE,
            hover_color=Colors.PRIMARY_HOVER,
            corner_radius=3,
            command=self.refresh
        )

        disconnect_button = CTkButton(
            self.page_content,
            width=120,
            height=30,
            fg_color=Colors.RED,
            text="Déconnexion",
            font=font_title(15),
            text_color=Colors.WHITE,
            hover_color="#802020",
            corner_radius=3,
            command=self.disconnect
        )

        disconnect_button.place(relx=0.8, y=30)
        refresh_button.place(relx=0.62, y=30)


    def refresh(self):
        for section in self.page_content.placed_item.winfo_children():
            section.load()
    
    def disconnect(self):
        with open("session.json", "w") as session:
            json.dump({}, session)
        
        login.LoginPage(self.window, self)
        
