from utils.ui import Colors, font_title, clear, place_page_top, font_text
from utils.getters import get_patient
from utils.objects import Patient, Prescription, Opinion, Stay
from pages import login
from config import session_json_path
from utils.textHandling import get_formated_text

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
            place_home_button=True,
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
        with open(session_json_path, "w") as session:
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
        title.grid(row=0, column=0, pady=10)

        self.main_frame = CTkScrollableFrame(
            self,
            width=220,
            fg_color=Colors.WHITE,
            height=420,
        )
        self.main_frame.grid(row=1, column=0, padx=6)

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
                (
                    f"Début: {stay.start}",
                    f"fin: {stay.end}",
                    f"Motif: {stay.reason}",
                    f"Docteur: Dr.{stay.doctor.last_name}",
                )
                for stay in patient.stays
            ]

        elif self.title == "Avis des médecins":
            info_list = [
                (opinion.title, opinion.description) for opinion in patient.opinions
            ]

        elif self.title == "Préscriptions":
            info_list = []
            for stay in patient.stays:
                prescription_details = [
                    f"- {drug['name']} : {drug['dosage']}"
                    for drug in stay.prescription.drugs
                    if drug
                ]

                if len(prescription_details):
                    info_list.append(prescription_details)

        if not info_list:
            CTkLabel(
                self,
                text="Liste est vide",
                text_color=Colors.SILVER,
                font=font_title(18),
            ).place(relx=0.5, y=80, anchor=CENTER)
            return

        for index, card_texts in enumerate(info_list):
            card = CTkFrame(
                self.main_frame,
                corner_radius=3,
                height=70,
                width=230,
                fg_color=Colors.WHITE,
                border_color=Colors.SILVER,
                border_width=1.1,
            )
            card.pack(fill="x", pady=6)

            for i, card_text in enumerate(card_texts):
                card_label = CTkLabel(
                    card,
                    font=font_text(11) if self.title=="Avis des médecins" and i==1 else font_title(12),
                    fg_color=Colors.WHITE,
                    text_color=Colors.SECONDARY_LIGHT if self.title=="Avis des médecins" and i==1 else Colors.SECONDARY,
                    text=get_formated_text(card_text, 30),
                )
                card_label.pack(pady=2)
