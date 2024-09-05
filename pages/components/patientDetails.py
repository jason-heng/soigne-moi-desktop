from utils.ui import Colors, font_title, clear, place_page_top
from utils.getters import get_patient
from utils.objects import Patient, Prescription, Opinion, Stay
from pages import login

import json
from customtkinter import *


class PatientDetails(CTkFrame):
    def __init__(self, window: CTk, master: CTkFrame, patient_id: Patient, token: str):
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
        self.patient = get_patient(patient_id, self.token)
        self.page_content = self.master
        self.home_page = self.master.master

        self.view()

    def view(self):

        place_page_top(
            title=f"Informations de {self.patient.first_name} {self.patient.last_name}", 
            page_content=self.page_content, 
            disconnect=self.disconnect,
            handle_place_homepage=self.home_page.handle_place_homepage,
            place_home_button=True
        )

        stays_history = Section(
            self, self.token, self.patient, "Historique des séjours"
        )
        opinions = Section(self, self.token, self.patient, "Avis des médecins")
        prescriptions = Section(self, self.token, self.patient, "Préscriptions")

        stays_history.place(x=0, y=0, relheight=1, relwidth=0.29)
        opinions.place(x=250, y=0, relheight=1, relwidth=0.29)
        prescriptions.place(x=501, y=0, relheight=1, relwidth=0.29)


    def disconnect(self):
        with open("session.json", "w") as session:
            json.dump({}, session)

        login.LoginPage(self.window)



class Section(CTkFrame):
    def __init__(self, master: CTkFrame, token: str, patient: Patient, title: str):
        super().__init__(
            master,
            corner_radius=8,
            fg_color=Colors.WHITE,
            border_color=Colors.SILVER_LIGHT,
            border_width=1.5,
            height=500,
            width=260,
        )

        self.master = master
        self.title = title
        self.token = token
        self.patient = patient
        self.current_page_index = 0

        self.view()

    def view(self):
        title = CTkLabel(
            master=self,
            text=self.title,
            font=font_title(20),
            text_color=Colors.PRIMARY,
        )
        title.pack(pady=10)

        self.main_frame = CTkFrame(self, width=220, fg_color=Colors.WHITE)
        self.main_frame.pack(fill="both", expand=True, pady=5, padx=18)

        self.next_page_button = CTkButton(
            self,
            width=20,
            height=20,
            corner_radius=5,
            fg_color=Colors.PRIMARY,
            text=">",
        )

        self.load(patient=self.patient)

    def load(self, patient=None):

        clear(self.main_frame)

        if not patient:
            patient = get_patient(self.patient.id, self.token)

        if self.title == "Historique des séjours":
            info_list = [
                f"Début: {stay.start}\nfin: {stay.end}\nMotif: {stay.reason}\nDocteur: Dr.{stay.doctor.last_name}"
                for stay in patient.stays
            ]

        elif self.title == "Avis des médecins":
            info_list = [opinion.title for opinion in patient.opinions]

        elif self.title == "Préscriptions":
            info_list = []
            for stay in patient.stays:
                prescription_details = "\n".join(
                    [f"- {drug['name']}" for drug in stay.prescription.drugs if drug]
                )
                if prescription_details:
                    info_list.append(prescription_details)

        pages: list[list[Stay | Prescription | Opinion]] = []

        for info in info_list:
            if not pages or len(pages[-1]) == 4:
                pages.append([info])
            else:
                pages[-1].append(info)

        if not pages:
            CTkLabel(
                self,
                text="Liste est vide",
                text_color=Colors.SILVER,
                font=font_title(18),
            ).place(relx=0.5, y=80, anchor=CENTER)
            return

        for card_text in pages[self.current_page_index]:
            card = CTkFrame(
                self.main_frame,
                corner_radius=3,
                height=70,
                width=230,
                fg_color=Colors.WHITE,
                border_color=Colors.SILVER,
                border_width=1.1,
            )
            card_label = CTkLabel(
                card,
                font=font_title(12),
                fg_color=Colors.WHITE,
                text_color=Colors.SECONDARY,
                text=card_text,
            )

            card.pack(pady=6)
            card_label.place(x=10, y=4)

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
        self.next_page_button.lift(self.main_frame)

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
        self.next_page_button.lift(self.main_frame)

    def update(self, num):
        if num:
            self.current_page_index += num
            self.load()
