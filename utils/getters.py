import json
from utils.objects import Patient, Stay
import requests
from datetime import datetime, timedelta

from config import API_URL


def get_all_stays(token : str) -> list[Stay] | None:
    """
    return all the stays in the website database as a list containing
    the stays as Stay objects
    """

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


def get_patient_stays(patient_id : int, token : str) -> list[Stay]:
    """
    return all the stays of a specific patient database as a list containing
    the stays as Stay objects
    """

    stays_list = get_all_stays(token)
    patient_stays = []
    for stay in stays_list:
        if stay.patient.id == patient_id:
            patient_stays.append(stay)
    
    return patient_stays


def get_filtered_stays(token : str) -> dict[ str, list[Stay] ]:
    """
    returns stays filtered by their start and end dates
    return in the following form [ current_stays, today_comings, today_leaves ]
    """
    stays_list = get_all_stays(token)

    current_stays, today_comings, today_leaves = [], [], []
    today_date = datetime.now().date()

    for stay in stays_list:
        leave_date = stay.end + timedelta(days=1)

        if stay.start < today_date < stay.end:
            current_stays.append(stay)
        elif today_date == stay.start:
            today_comings.append(stay)
        elif today_date == leave_date:
            today_leaves.append(stay)

    return {"current" : current_stays, "today_comings" :  today_comings, "today_leaves" : today_leaves}


def get_patient(patient_id : str, token : str) -> Patient | None:
    """
    return all the stays in the website database as a list containing
    the stays as Stay objects
    """

    headers = {"Authorization": f"Bearer {token}"}
    req = requests.get(
        url=f"{API_URL}/secretary/patient/{patient_id}",
        headers=headers,
    )

    if req.status_code == 200:
        patient_info = req.json()["patient"]
        patient = Patient(patient_info, True)

        return patient

    return None

