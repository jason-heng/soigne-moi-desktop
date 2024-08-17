from utils.timeHandling import to_local_datetime

from datetime import datetime

class Patient:
    def __init__(self, patient_info : dict, full_patient: bool) -> None:
        self.id: int = patient_info["id"]
        self.first_name: str = patient_info["firstName"]
        self.last_name: str = patient_info["lastName"]

        if full_patient:
            self.opinions: list[Opinion] = [Opinion(opinion_info) for opinion_info in patient_info["opinions"]]
            self.stays: list[Stay] = [Stay(stay_info, patient=self) for stay_info in patient_info["stays"]]



class Doctor:
    def __init__(self, doctor_info) -> None:
        self.first_name = doctor_info["firstName"]
        self.last_name = doctor_info["lastName"]



class Stay:
    def __init__(self, stay_info : dict, patient : Patient | None = None) -> None:
        self.id : int = stay_info["id"]
        self.patient = patient if patient else Patient(stay_info["patient"], False)
        self.doctor = Doctor(stay_info["doctor"])
        self.reason : str = stay_info["reason"]
        self.start = to_local_datetime(stay_info["start"])
        self.end = to_local_datetime(stay_info["end"])
        self.prescription = Prescription(stay_info["prescription"])


class Secretary:
    def __init__(self, secretary_info : dict) -> None:
        self.id : int = secretary_info["id"]
        self.first_name = secretary_info["firstName"]
        self.last_name = secretary_info["lastName"]


class Opinion:
    def __init__(self, opinion_info : dict) -> None:
        self.doctor = Doctor(opinion_info["doctor"])
        self.title : str = opinion_info["title"]
        self.description : str = opinion_info["description"]



class Drug:
    def __init__(self, drug_info : dict) -> None:
        self.name = drug_info["name"]
        self.dosage = drug_info["dosage"]



class Prescription:
    def __init__(self, prescription_info : dict) -> None:
        self.start = to_local_datetime(prescription_info["start"])
        self.end: datetime = to_local_datetime(prescription_info["end"])
        self.drugs: list[Drug] = prescription_info["end"]