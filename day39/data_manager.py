import requests
from requests.auth import HTTPBasicAuth
import json

class DataManager:
    def __init__(self) -> None:
        self.url = "https://api.sheety.co/d68ffc8da2b9b56f0fe4908595a915ca/flightDeals/prices"
        self.username = "vibakar"
        self.password = "vibakar2394"
    
    def get_data_from_spreadsheet(self):
        basic = HTTPBasicAuth(self.username, self.password)
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(self.url, headers=headers, auth=basic)
        return response.json()["prices"]
    
    def update_spreadsheet(self, id, row):
        body = {
            "price": row
        }
        basic = HTTPBasicAuth(self.username, self.password)
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(f"{self.url}/{id}", headers=headers, data=json.dumps(body), auth=basic)
        return response.json()