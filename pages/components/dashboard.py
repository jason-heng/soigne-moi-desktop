import threading
from customtkinter import *
from utils.ui import (
    Colors,
    font_title,
    clear,
    font_text,
    change_button_text_color,
    place_loading_frame,
)
from utils.getters import *
from pages.components.patientDetails import PatientDetails


class HomeDashboard(CTkFrame):
    def __init__(self, window: CTk, master: CTkFrame, token: str, stays=None):
        super().__init__(
            master,
            corner_radius=0,
            fg_color=Colors.TERTIARY,
            height=500,
            width=833,
        )

        self.window = window
        self.master = master
        self.token = token
        self.stays_list = stays
        if not self.stays_list:
            self.stays_list = get_filtered_stays(token=self.token)

        self.view()

    def view(self):
        enteries = PatientSection(
            self.window, self, self.token, "Entrées", 1, self.stays_list
        )
        leaves = PatientSection(
            self.window, self, self.token, "Sorties", 2, self.stays_list
        )
        current = PatientSection(
            self.window, self, self.token, "Séjours en cours", 0, self.stays_list
        )

        enteries.place(x=0, y=0, relheight=1, relwidth=0.29)
        leaves.place(x=250, y=0, relheight=1, relwidth=0.29)
        current.place(x=501, y=0, relheight=1, relwidth=0.29)


class PatientSection(CTkFrame):
    def __init__(
        self,
        window: CTk,
        master: CTkFrame,
        token: str,
        title: str,
        type_index: int,
        stays_list,
    ):
        super().__init__(
            master,
            corner_radius=8,
            fg_color=Colors.WHITE,
            border_color=Colors.SILVER_LIGHT,
            border_width=1.5,
            height=500,
            width=260,
        )

        self.window = window
        self.master = master
        self.title = title
        self.token = token
        self.type_index = type_index
        self.current_page_index = 0
        self.stays_list = stays_list

        self.view()

    def view(self):
        title = CTkLabel(
            master=self,
            text=self.title,
            font=font_title(20),
            text_color=Colors.PRIMARY,
        )
        title.pack(pady=10)

        self.patients_frame = CTkFrame(self, width=220, fg_color=Colors.WHITE)
        self.patients_frame.pack(fill="both", expand=True, pady=5, padx=18)

        self.next_page_button = CTkButton(
            self,
            width=20,
            height=20,
            corner_radius=5,
            fg_color=Colors.PRIMARY,
            text=">",
        )

        self.load(self.stays_list)

    def load(self, stays_list=None):
        clear(self.patients_frame)

        if not stays_list:
            stays_list = get_filtered_stays(self.token)

        stays = stays_list[self.type_index]
        pages: list[list[Stay]] = []

        button_paths = {}
        self.patient_buttons = {}

        for stay in stays:
            if not pages or len(pages[-1]) == 4:
                pages.append([stay])
            else:
                pages[-1].append(stay)

        if not pages:
            CTkLabel(
                self,
                text="Liste est vide",
                text_color=Colors.SILVER,
                font=font_title(18),
            ).place(relx=0.5, y=80, anchor=CENTER)
            return

        for stay in pages[self.current_page_index]:
            patient_card = CTkFrame(
                self.patients_frame,
                corner_radius=3,
                height=70,
                width=230,
                fg_color=Colors.WHITE,
                border_color=Colors.SILVER,
                border_width=1.1,
            )
            card_title = CTkLabel(
                patient_card,
                font=font_title(18),
                fg_color=Colors.WHITE,
                text_color=Colors.SECONDARY,
                text=f"{stay.patient.first_name} {stay.patient.last_name}",
            )
            card_title.bind(
                "<ButtonPress-1>",
                lambda e: self.handle_patient_button(
                    self.master.master, str(e.widget), self.token
                ),
            )

            button_paths[str(card_title)] = card_title
            self.patient_buttons[str(card_title)] = stay.patient.id

            card_title.bind(
                "<Enter>",
                lambda e: change_button_text_color(
                    str(e.widget), button_paths, Colors.PRIMARY
                ),
            )
            card_title.bind(
                "<Leave>",
                lambda e: change_button_text_color(
                    str(e.widget), button_paths, Colors.SECONDARY
                ),
            )

            motif = [chara for chara in f"""Motif: "{stay.reason}" """]
            if len(motif) > 35:
                motif = motif[:32]
                motif.append("...")

            card_reason = CTkLabel(
                patient_card,
                font=font_text(12),
                text_color=Colors.SECONDARY_LIGHT,
                text="".join(motif),
            )
            patient_card.pack(pady=6)
            card_title.place(x=10, y=6)
            card_reason.place(x=10, y=32)

        pages_number = len(pages) - 1

        button_fg_color = (
            Colors.SILVER if self.current_page_index == pages_number else Colors.PRIMARY
        )
        button_hover_color = (
            Colors.PRIMARY_HOVER
            if self.current_page_index < pages_number
            else Colors.SILVER
        )

        self.next_page_button = CTkButton(
            self,
            text=">",
            font=font_title(22),
            height=30,
            width=30,
            fg_color=button_fg_color,
            corner_radius=2,
            hover_color=button_hover_color,
            command=lambda: self.update(
                +1 if self.current_page_index < pages_number else 0
            ),
        )
        self.next_page_button.place(x=200, y=450)
        self.next_page_button.lift(self.patients_frame)

        self.previous_page_button = CTkButton(
            self,
            text="<",
            font=font_title(22),
            height=30,
            width=30,
            fg_color=Colors.PRIMARY if self.current_page_index else Colors.SILVER,
            corner_radius=2,
            hover_color=(
                Colors.PRIMARY_HOVER if self.current_page_index else Colors.SILVER
            ),
            command=lambda: self.update(-1 if self.current_page_index else 0),
        )
        self.previous_page_button.place(x=20, y=450)
        self.next_page_button.place(x=200, y=450)
        self.next_page_button.lift(self.patients_frame)


    def handle_patient_button(self, page_content, widget_str, token):
        process_thread = threading.Thread(
            target=lambda: self.place_patient_details(page_content, widget_str, token)
        )
        process_thread.start()
        place_loading_frame(page_content)


    def place_patient_details(self, page_content, widget_str: str, token: str):
        for button_str in list(self.patient_buttons):
            if widget_str.startswith(button_str):
                widget_str = button_str

        patient_id = self.patient_buttons[widget_str]

        patient_details = PatientDetails(self.window, page_content, patient_id, token)
        page_content.placed_item = patient_details
        patient_details.place(x=0, y=88)

    def update(self, num):
        if num:
            self.current_page_index += num
            self.load()
