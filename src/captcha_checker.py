import os
import requests

RECAPTCHA_SECRET_KEY = os.getenv("recaptcha_api", "")
URL = "https://www.google.com/recaptcha/api/siteverify"

def checker(key):
    result = requests.post(
        URL,
        data={
            "secret": RECAPTCHA_SECRET_KEY,
            "response": key
        }
    )

    if result.status_code == 200:
        result = result.json()
        return result["success"]
    else:
        return False
