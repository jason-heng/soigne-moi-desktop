from datetime import datetime

class Patient:
    def __init__(self, user_id):
        self.id = user_id
        self.first_name = "hamid"
        self.last_name = "lepatient"
        self.email = "hamidLepatient@gmail.com"
        self.adress = "21 rue duchantier"
        self.is_admin = False
        self.stays = [
            Stay(63, patient=self),
            Stay(62, patient=self),
            Stay(6, patient=self),
            Stay(636, patient=self),
            Stay(630, patient=self),
        ]

class Stay:
    def __init__(self, stay_id : int, patient: Patient | None = None):
        self.id = stay_id
        self.patient = patient if patient else Patient(96)
        self.patient_id = patient.id
        self.start = "20/11/2022"
        self.end = "25/11/2022"
        self.reason = "pharingite"

