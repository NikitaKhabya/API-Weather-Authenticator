api_key="1bb80f843fb8773111d7041b78178141"
import requests
from twilio.rest import Client
account_sid="AC224424ad1403ced3521ff1bee7e08174"
auth_token="e84e0071a70fa40e2be19b98f7ba3535"
MY_LAT=19.075983
MY_LNG=72.877655

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
        from_="+12566766828",
        to="+919136317934"
    )
    print(message.status)



