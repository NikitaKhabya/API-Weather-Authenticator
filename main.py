api_key="your api key from open weather API" //use your own api_key
import requests
from twilio.rest import Client
account_sid="your account sid from twilio" //use your own account sid
auth_token="your auth token from twilio" //use your own auth_token   
MY_LAT=19.075983   //latitude of location you are at
MY_LNG=72.877655    //longitude of location you are at

parameters={
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid":api_key,
    "exclude":"currently,minutely,daily"
}
response=requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data=response.json()

will_rain=False
weather_slice=data["hourly"][:12]
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today. Remember to bring an umbrella!! .",
        from_="+your twilio number",
        to="+Your number"
    )
    print(message.status)



