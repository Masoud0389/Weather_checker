import requests
from twilio.rest import Client


api_key = "your open weather map api key"
hourly_forcast_url = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
LAT = 45.462638  # your location LATITUDE
LON = -73.631576  # your location LONGITUDE
twilio_account_id = "your twilio account id"
twilio_auth_token = "your twilio authentication token"
twilio_recovery_code = "your twilio recovery code"
SID = "your SID"
Secret_code = "your Secret code"
weather_parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
}
response = requests.get(url=current_weather_url, params=weather_parameters)
response.raise_for_status()
data = response.json()
weather_code = data["weather"][0]["id"]
if weather_code < 700:
    print("Bring an umbrella!")  # you can type any other messages here


############################
client = Client(twilio_account_id, twilio_auth_token)
message = client.messages.create(
                              body='Hi there, I am Masoud from twilio.',
                              from_="twilio phone number",
                              to='your phone number',
                          )
print(message.sid)
