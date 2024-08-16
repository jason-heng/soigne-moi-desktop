import requests
from config import API_URL
import json

def login_verif(email : str, password : str) -> dict[str, str | None] :
    try:
        req = requests.post(
            url=f"{API_URL}/secretary/auth",
            json={"email" : email, "password" : password}
        )
    except requests.exceptions.ConnectionError:
        return {"error_text" : "Veuillez verifier votre connexion internet", "token" : None} 
        
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


