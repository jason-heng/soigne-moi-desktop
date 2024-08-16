import json
from utils.objects import Patient, Stay
import requests

from config import API_URL


def get_all_stays(token : str) -> list[Stay] | None:
    headers = {"Authorization": f"Bearer {token}"}
    req = requests.get(
        url=f"{API_URL}/secretary/stays",
        headers=headers,
    )
    stays_list = []

    for stay_info in req.json()["stays"]:
        stay = Stay(stay_info)
        stays_list.append(stay)

    return stays_list


def get_all_patients(token : str) -> list[Patient] | None:
    stays_list = get_all_stays(token)
    patients_list = []
    for stay in stays_list:
        if stay.patient not in patients_list:
            patients_list.append(stay.patient)

    return patients_list


def get_patient_stays(patient_id, token) -> list[Stay]:
    stays_list = get_all_stays(token)
    patient_stays = []
    for stay in stays_list:
        if stay.patient.id == patient_id:
            patient_stays.append(stay)
    
    return patient_stays


def get_patient(patient_id, token) -> Patient | None:
    return []

