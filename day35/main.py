import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast/"
api_key = os.environ.get("API_KEY")

weather_params = {
    "lat": 38.7272,
    "lon": 139.8267,
    "appid": api_key,
    "cnt": 4
}
OWN_response = requests.get(OWN_Endpoint, params=weather_params)
OWN_response.raise_for_status()

weather_data = OWN_response.json()
for _ in range(4):
    weather_code = weather_data["list"][_]["weather"][0]["id"]
    if weather_code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain.",
            from_="+12314473502",
            to="+639665481579"
        )
        print(message.sid)