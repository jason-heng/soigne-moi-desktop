from customtkinter import *
from utils.ui import Colors, font_title, font_text, clear, change_button_text_color
from utils.getters import *
import tkinter

class PatientsList(CTkFrame):
    def __init__(self, master: CTkFrame, token: str):
        super().__init__(master, corner_radius = 0, fg_color = Colors.TERTIARY_LIGHT)

        self.master  =  master
        self.window  =  master.window
        self.token = token
        self.current_page_index  =  0
        self.SelectedPatient  =  None
        self.patients = get_all_patients(token=self.token)

        self.view()

    def view(self):
        header  =  CTkFrame(self, fg_color = Colors.TERTIARY, corner_radius = 0, height = 75)
        header.pack(fill = "x")

        CTkLabel(
            header, 
            text = "Liste des patients", 
            font = font_title(24), 
            text_color = Colors.PRIMARY
        ).place(relx=0.435, y=35, anchor=CENTER)

        self.searchPatient  =  CTkEntry(
            self,
            placeholder_text = "Rechercher un patient...",
            height = 29,
            width=300,
            font = font_title(12),
            text_color = Colors.SECONDARY,
            fg_color = Colors.WHITE,
            border_color="#b5b5b5",
            border_width = 1,
            corner_radius = 4,
        )
        self.searchPatient.place(relx=0.5, y=75, anchor=CENTER)

        self.patients_frame = CTkFrame(self, fg_color = Colors.TERTIARY)
        self.patients_frame.pack(fill = "both", expand = True, pady=20)

        self.searchPatient.bind("<Key>", lambda _: self.load("typing"))
        self.searchPatient.bind("<Return>", lambda _: self.load("returning"))
        
        self.load()


    def load(self, action=None):
        clear(self.patients_frame)

        patients = self.patients
        pages : list[list[Patient]] = []
        search = self.searchPatient.get()[:-1] if action=="returning" else self.searchPatient.get()

        if not patients:
            CTkLabel(self, text = "Aucun patient", text_color = Colors.SECONDARY, font = font_title(24)).place(relx = 0.5, rely = 0.5, anchor = CENTER)
            return

        for patient in patients:
            if not pages or len(pages[-1]) == 5:
                pages.append([])
            if search and len(search) > 1:
                if search in f"{patient.first_name.lower()} {patient.last_name.lower()}":   
                    pages[-1].append(patient)
            else:
                pages[-1].append(patient)

        self.patient_buttons = {}
        button_paths = {}

        for patient in pages[self.current_page_index]:
            patient_card  =  CTkFrame(
                self.patients_frame,
                width = 300,
                height = 75,
                corner_radius = 9,
                fg_color = Colors.TERTIARY,
                border_width=1.2,
                border_color="#b5b5b5",
            )
            patient_card.pack(pady = 10)

            patient_button = CTkButton(
                patient_card,
                text = f"{patient.first_name.capitalize()} {patient.last_name.capitalize()}",
                font = font_title(16),
                corner_radius = 15,
                height = 41,
                width = 35 * len([patient.first_name, patient.last_name]),
                hover_color = Colors.TERTIARY,
                text_color = Colors.SECONDARY,
                fg_color = Colors.TERTIARY,
                command = lambda: None,
            )

            button_paths[str(patient_button)] = patient_button
            
            patient_button.bind("<Enter>", lambda e: change_button_text_color(str(e.widget), button_paths, Colors.PRIMARY))
            patient_button.bind("<Leave>", lambda e: change_button_text_color(str(e.widget), button_paths, Colors.SECONDARY))
            patient_button.place(x = 5, y = 7)

            self.patient_buttons[patient_button] = patient.id

            CTkLabel(
                patient_card,
                text = f"nombre de séjours: {len(patient.stays)}",
                font = font_text(12),
                text_color = Colors.PRIMARY,
            ).place(x = 21, y = 40)

        page_management_frame = CTkFrame(self, fg_color=Colors.TERTIARY, height=35, width=110)
        page_management_frame.place(rely=0.95, relx=0.5, anchor=CENTER)

        CTkButton(
            page_management_frame,
            text = "<",
            font = font_title(22),
            height = 33,
            width = 33,
            fg_color = Colors.PRIMARY if self.current_page_index else Colors.SILVER,
            corner_radius = 3,
            hover_color = Colors.PRIMARY_HOVER if self.current_page_index else Colors.SILVER,
            command = lambda: self.update(-1 if self.current_page_index else 0),
        ).place(x=0, y=0)

        CTkLabel(
            page_management_frame,
            text = self.current_page_index + 1,
            font = font_title(24),
            text_color = Colors.SECONDARY,
        ).place(relx=0.5, rely=0.5, anchor=CENTER)

        pages_number = len(pages) - 1
        button_fg_color = Colors.PRIMARY if self.current_page_index < pages_number else Colors.SILVER
        button_hover_color = Colors.PRIMARY_HOVER if self.current_page_index < pages_number else Colors.SILVER
        CTkButton(
            page_management_frame,
            text = ">",
            font = font_title(22),
            height = 33,
            width = 33,
            fg_color = button_fg_color,
            corner_radius = 3,
            hover_color = button_hover_color,
            command = lambda: self.update(+1 if self.current_page_index < pages_number else 0),
        ).place(x=73, y=0)


    def update(self, num):
        if num:
            self.current_page_index +=  num
            self.load()
        if self.SelectedPatient:
            for patient_buttons in self.patient_buttons:
                if self.SelectedPatient == self.patient_buttons[patient_buttons]:
                    self.select(patient_buttons)