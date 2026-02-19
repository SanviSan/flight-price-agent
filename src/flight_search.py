import requests
import json
from src.amadeus_client import get_amadeus_token

def search_flights():
    token = get_amadeus_token()

    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    params = {
        "originLocationCode": "LHR",
        "destinationLocationCode": "BLR",
        "departureDate": "2026-07-20",
        "returnDate": "2026-08-07",
        "adults": 1,
        "currencyCode": "GBP",
        "max": 10
    }

    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()

    data = r.json()
    #print(json.dumps(data, indent=2))  # Debugging: print the entire response
    flights = data.get("data", [])

    if not flights:
        raise ValueError("No flights found in the response.")

    cheapest = min(flights, key=lambda x: float(x["price"]["grandTotal"]))
    return cheapest