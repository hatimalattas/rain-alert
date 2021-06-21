import requests
from twilio.rest import Client

account_sid = "AC6eb18c5e535659edba411de85a8fa7f7"
auth_token = "920bf2bde00c94d5ec8ce6393be18e1d"
client = Client(account_sid, auth_token)

parameters = {
    "appid": "081d1e0b050b7f67678b085771f98aff",
    "lat": 35.779591,
    "lon": -78.638176,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"]
hourly_data_id = []

for i in range(0, 12):
    hourly_data_id.append(hourly_data[i]["weather"][0]["id"])
# print(hourly_data_id)

will_rain = False

for weather_id in hourly_data_id:
    if weather_id < 700:
        will_rain = True
        break

if will_rain:
    # print("It's going to rain today. Remember to bring an ☂️.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_='+14356339025',
        to='+966566131333'
    )
    print(message.status)
