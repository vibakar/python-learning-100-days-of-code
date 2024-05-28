from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

sheet_data = data_manager.get_data_from_spreadsheet()
for data in sheet_data:
    if data["iataCode"] == "":
        data["iataCode"] = flight_search.get_destination_code(data["city"])
        response = data_manager.update_spreadsheet(data["id"], data)
        print(response)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
