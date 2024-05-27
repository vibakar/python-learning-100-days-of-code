import requests
import json
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD =  os.environ["SHEETY_PASSWORD"]

def write_to_spreadsheet(exercise_stats):
    url = 'https://api.sheety.co/d68ffc8da2b9b56f0fe4908595a915ca/newWorkouts/workouts';
    body = {
        "workout": {
            "date": datetime.now().strftime("%d/%M/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise_stats["user_input"].title(),
            "duration": exercise_stats["duration_min"],
            "calories": exercise_stats["nf_calories"]
        }
    }
    basic = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, data=json.dumps(body), auth=basic)
    print(response.json())

def get_exercise_stats():
    user_input = input("Tell me which exercise you did: ")
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "0"
    }
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    data = {
        "query": user_input
    }
    response = requests.post(url=url, headers=headers, data=data)
    return response.json()["exercises"][0]

exercise_stats = get_exercise_stats()
write_to_spreadsheet(exercise_stats)
