from customtkinter import *
from utils.ui import Colors, font_title
from utils.logic import *


class PatientCard(CTkFrame):
    def __init__(self, master : CTkFrame, patient: Patient):
        super().__init__(master, corner_radius = 5, fg_color = Colors.SECONDARY, border_color = Colors.LIGHT_GRAY)
        CTkLabel(self, fg_color=Colors.PRIMARY, text="patients info", font=font_title(50))
        self.master  =  master
        self.window  =  master.window
        self.currentPage  =  0
        self.SelectedPatient  =  None

        self.view()
    
    def view(self):
        pass

class PatientsList(CTkScrollableFrame):
    def __init__(self, master: CTkFrame):
        super().__init__(master, corner_radius = 0, fg_color = Colors.PRIMARY)

        self.master  =  master
        self.window  =  master.window
        self.currentPage  =  0
        self.SelectedPatient  =  None

        self.view()

    def view(self):
        patients_list = get_all_patients()
        pos_y = 0
        for patient in patients_list:
            patient_card = PatientCard(self, patient)
            patient_card.place(relwidth=0.8, relheight=0.1, relx=0.5, anchor=CENTER, y=pos_y)

            pos_y += 50