import requests
import json
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

x_app_id = os.getenv('X_APP_ID')
x_app_key = os.getenv('X_APP_KEY')
authorization = os.getenv('AUTHORIZATION')
url_sheety = os.getenv('url_sheety')

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': x_app_id,
    'x-app-key': x_app_key,
}

body = {
    "query": "ran for 30 min"
}

response = requests.post(url=url, headers=headers, data=json.dumps(body))
response = response.json()
now = datetime.datetime.now()

formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H:%M:%S")
exercises = response['exercises'][0]


headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
}
url_sheety = "https://api.sheety.co/" + url_sheety
response = requests.get(url_sheety, headers=headers)


payload = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercises["name"],
        "duration": exercises["duration_min"],
        "calories": exercises["nf_calories"],
    }
}
response_post = requests.post(
    url_sheety, data=json.dumps(payload), headers=headers)
print("response_post: ", response_post)
