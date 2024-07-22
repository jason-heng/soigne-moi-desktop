from utils.objects import Patient, Stay
from random import randint

def get_all_stays() -> list[Stay] | None:
    return []

def get_all_patients() -> list[Patient] | None:
    patients_list = [Patient(randint(0, 100)) for i in range(20)]
    return patients_list

def get_stay(stay_id) -> Stay | None:
    return []

def get_patient_stays(patient_id) -> list[Stay]:
    return []

def get_patient(patient_id) -> Patient | None:
    return []

