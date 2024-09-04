import threading
from utils.ui import Colors, focus_event, place_page_top, place_loading_frame, clear
from utils.getters import *
from pages.components.patientsList import PatientsList
from pages.components.dashboard import HomeDashboard
from utils.objects import Secretary
from pages import login

from customtkinter import *


class PageContent(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Colors.TERTIARY, width=770, corner_radius=0)
        self.placed_item: CTkFrame | None = None


class HomePage(CTkFrame):
    def __init__(
        self, window: CTk, token: str, secretary: Secretary, past_page: CTkFrame = None
    ) -> None:
        self.past_page = past_page
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

        self.home_dashboad = HomeDashboard(self.page_content, self.token)
        self.home_dashboad.place(x=0, y=88)
        self.page_content.placed_item = self.home_dashboad

        place_page_top(
            title="Informations du jour", 
            page_content=self.page_content, 
            disconnect=self.disconnect, 
            refresh=self.refresh,
            handle_place_homepage=self.handle_place_homepage, 
            place_home_button=False
        )
    

    def handle_place_homepage(self):
        def replace_home_page():
            self.home_dashboad = HomeDashboard(self.page_content, self.token)
            
            place_page_top(
            title="Informations du jour", 
            page_content=self.page_content, 
            disconnect=self.disconnect, 
            refresh=self.refresh,
            handle_place_homepage=self.handle_place_homepage,
            place_home_button=False
        )
            self.home_dashboad.place(x=0, y=88)

        place_loading_frame(self.page_content)
        process_thread = threading.Thread(target=replace_home_page)
        process_thread.start()
        


    def refresh(self):
        for section in self.page_content.placed_item.winfo_children():
            section.load()


    def disconnect(self):
        with open("session.json", "w") as session:
            json.dump({}, session)

        login.LoginPage(self.window, self)
