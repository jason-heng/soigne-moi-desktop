from datetime import datetime

class Patient:
    def __init__(self, patient_info : dict) -> None:
        self.id = patient_info["id"]
        self.first_name = patient_info["firstName"]
        self.last_name = patient_info["lastName"]
        self.opinions = patient_info["opinions"]
        


class Doctor:
    def __init__(self, doctor_info) -> None:
        self.first_name = doctor_info["firstName"]
        self.last_name = doctor_info["lastName"]



class Stay:
    def __init__(self, stay_info : dict) -> None:
        self.id : int = stay_info["id"]
        self.patient = Patient(stay_info["patient"])
        self.doctor = Doctor(stay_info["doctor"])
        self.reason : str = stay_info["reason"]
        self.start = datetime.strptime(stay_info["start"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.end = datetime.strptime(stay_info["end"], "%Y-%m-%dT%H:%M:%S.%fZ")
