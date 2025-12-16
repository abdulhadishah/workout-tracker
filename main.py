import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

NIX_APP_ID = os.environ["NIX_APP_ID"]
NIX_API_KEY = os.environ["NIX_API_KEY"]
NIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

nix_header = {
    "x-app-id": NIX_APP_ID,
    "x-app-key": NIX_API_KEY
}

exercise_input = input("Tell me which exercise you did: ")

nix_payload = {"query": exercise_input}

nix_response = requests.post(url=NIX_ENDPOINT, headers=nix_header, json=nix_payload)

nix_data = nix_response.json()

exercise_name = nix_data["exercises"][0]["user_input"].title()
exercise_duration = nix_data["exercises"][0]["duration_min"]
calories_burned = nix_data["exercises"][0]["nf_calories"]

today_date= datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

workout_entry = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": calories_burned
    }
}

sheety_header = {
    "Authorization": os.environ["AUTHORIZATION"]
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=workout_entry, headers=sheety_header)
print(sheety_response.text)