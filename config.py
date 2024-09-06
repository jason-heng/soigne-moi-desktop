from dotenv import load_dotenv
import json
from os import environ as env
import os

local_appdata_path = os.getenv('LOCALAPPDATA')

session_json_path = os.path.join(local_appdata_path, 'session.json')

load_dotenv(override=True)
API_URL = env["API_URL"]


def get_token() -> str | None:
    with open(session_json_path, "r") as file:
        session = json.load(file)
    return session if session else None
