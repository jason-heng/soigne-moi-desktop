import threading
from utils.ui import (
    Colors,
    focus_event,
    place_page_top,
    place_loading_frame,
    clear,
    place_loading_frame_fullpage,
)
from utils.getters import *
from pages.components.patientsList import PatientsList
from pages.components.dashboard import HomeDashboard
from utils.objects import Secretary
from pages import login
from config import session_json_path

from customtkinter import *


class PageContent(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Colors.TERTIARY, width=770, corner_radius=0)
        self.placed_item: CTkFrame | None = None


class HomePage(CTkFrame):
    def __init__(self, window: CTk, token: str, secretary: Secretary) -> None:
        clear(window)

        super().__init__(window, corner_radius=0, fg_color=Colors.TERTIARY)
        self.pack(fill="both", expand=True)
        self.window = window
        self.token = token
        self.secretary = secretary

        self.view()
        focus_event(self.window)

    def prepare_informations(self):
        self.patients_list = get_all_patients(token=self.token)
        self.stays = get_filtered_stays(self.token)

    def place_components(self):
        try:
            for w in self.loading_frames:
                w.destroy()
        except:
            pass

        self.ctk_patients_list = PatientsList(
            self.window, self, self.token, self.patients_list
        )
        self.home_dashboad = HomeDashboard(
            self.window, self.page_content, self.token, self.stays
        )

        self.page_content.pack(fill="y", side=RIGHT)
        self.ctk_patients_list.place(relheight=1, relwidth=0.3, x=0, y=0)
        self.home_dashboad.place(x=0, y=88)
        self.page_content.placed_item = self.home_dashboad

        place_page_top(
            title="Informations du jour",
            page_content=self.page_content,
            disconnect=self.disconnect,
            handle_place_homepage=self.handle_place_homepage,
            place_home_button=False,
        )

    def view(self):
        process_thread = threading.Thread(target=self.prepare_informations)
        process_thread.start()

        self.page_content = PageContent(self)
        self.loading_frames = place_loading_frame_fullpage(self.window)

        while True:
            try:
                self.patients_list
                self.stays
                break
            except AttributeError:
                continue

        self.place_components()

    def handle_place_homepage(self):
        def replace_home_page():
            self.home_dashboad = HomeDashboard(
                self.window, self.page_content, self.token
            )

            place_page_top(
                title="Informations du jour",
                page_content=self.page_content,
                disconnect=self.disconnect,
                handle_place_homepage=self.handle_place_homepage,
                place_home_button=False,
            )
            self.home_dashboad.place(x=0, y=88)

        place_loading_frame(self.page_content)
        process_thread = threading.Thread(target=replace_home_page)
        process_thread.start()

    def disconnect(self):
        with open(session_json_path, "w") as session:
            json.dump({}, session)

        login.LoginPage(self.window)
