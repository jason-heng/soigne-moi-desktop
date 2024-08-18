from config import API_URL
from utils.objects import Secretary

import json
import requests

def login_verif(email : str, password : str) -> dict[str, str | None] :
    try:
        req = requests.post(
            url=f"{API_URL}/secretary/auth",
            json={"email" : email, "password" : password}
        )
    except requests.exceptions.ConnectionError:
        return {"error_text" : "Veuillez verifier votre connexion internet", "token" : None, "secretary": None} 

    if req.status_code == 200:
        token = req.json()["token"]
        secretary_info = req.json()["secretary"] 
        error_text = None
    else:
        token, secretary_info = None, None
        try:
            errors_dict = req.json()["errors"]
            error_key = list(errors_dict)[0]
            error_text = errors_dict[error_key]
        except KeyError:
            error_text = "something went wrong, try again later"

    return {"error_text" : error_text, "token" : token, "secretary" : secretary_info}
        

def update_token(token : str, secretary_info: dict) -> None:
    with open("session.json", "w") as file:
        json.dump({"token" : token, "secretary": secretary_info}, file)


