import requests
from datetime import datetime

# ------------------ GET ISS POSITION ------------------ #
iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()

latitude = float(iss_data["iss_position"]["latitude"])
longitude = float(iss_data["iss_position"]["longitude"])

# ------------------ GET SUNRISE / SUNSET TIMES ------------------ #
parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

# ------------------ GET CURRENT TIME ------------------ #
current_hour = datetime.utcnow().hour   # Use UTC because the API returns UTC time

# ------------------ CHECK DAY OR NIGHT ------------------ #
if sunrise <= current_hour <= sunset:
    status = "DAYTIME ☀️"
else:
    status = "NIGHTTIME 🌙"

# ------------------ PRINT RESULTS ------------------ #
print("ISS CURRENT POSITION")
print("--------------------")
print(f"Latitude : {latitude}")
print(f"Longitude: {longitude}")
print()

print("SUN INFORMATION (UTC)")
print("--------------------")
print(f"Sunrise Hour: {sunrise}")
print(f"Sunset Hour : {sunset}")
print(f"Current Hour: {current_hour}")
print()

print("STATUS")
print("------")
print(status)
