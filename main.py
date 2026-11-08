
import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Asteroid:
    def __init__(self, name, diameter, dangerous):
        self.name = name
        self.diameter = diameter
        self.dangerous = dangerous

    def show(self):
        print("Name:", self.name)
        print("Diameter:", round(self.diameter, 2), "km")
        print("Potentially Hazardous:", self.dangerous)
        print("------------------------")


api_key = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/neo/rest/v1/feed"

params = {
    "api_key": api_key,
    "start_date": "2025-09-07",
    "end_date": "2025-09-07"
}

try:
    response = requests.get(url, params=params, timeout=20)
    print("HTTP Status:", response.status_code)
    response.raise_for_status()

    data = response.json()
    asteroids = []

    for item in data["near_earth_objects"]["2025-09-07"]:
        asteroid = Asteroid(
            item["name"],
            item["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
            item["is_potentially_hazardous_asteroid"]
        )
        asteroids.append(asteroid)

    print("\nNASA Asteroids Report")
    print("========================")

    for asteroid in asteroids:
        asteroid.show()

except requests.RequestException as error:
    print("NASA request failed:", error)
    if "response" in locals():
        print("Response:", response.text[:300])
