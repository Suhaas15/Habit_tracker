import requests
from datetime import datetime

from Habit_Tracking.update_pixela import PIXELA_TOKEN

pixela_endpoint="https://pixe.la/v1/users"

TOKEN=PIXELA_TOKEN
USERNAME="suhaas15"
GRAPH_ID = "graph1"

user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)       #https://pixe.la/@suhaas15
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "questions",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)        #https://pixe.la/v1/users/suhaas15/graphs/graph1.html
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.now().strftime("%Y%m%d")
pixel_data={
    "date": today,
    "quantity": input("How many coding problems did you solve today?"),
}

response=requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
print(response.text)