from dotenv import load_dotenv
import json
from os import environ as env

load_dotenv(override=True)
API_URL = env["API_URL"]

def get_token() -> str | None:
    with open("session.json", "r") as file:
        session = json.load(file)
    return session if session else None
