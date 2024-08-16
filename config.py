from dotenv import load_dotenv

load_dotenv(override=True)

from os import environ as env

API_URL = env["API_URL"]
