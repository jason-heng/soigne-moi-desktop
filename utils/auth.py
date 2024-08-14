import requests
from config import API_URL
import json

def login_verif(email : str, password : str) -> dict[str, str | None] :
    req = requests.post(
        url=API_URL,
        json={"email" : email, "password" : password}
    )
    token = req.json()["token"] if req.status_code == 200 else None

    try:
        errors_dict = req.json()["errors"]
        error_key = list(errors_dict)[0]
        error_text = errors_dict[error_key]
    except KeyError:
        error_text = None

    return {"error_text" : error_text, "token" : token}
        

def update_token(token : str) -> None:
    with open("session.json", "w") as file:
        json.dump({"token" : token}, file)


