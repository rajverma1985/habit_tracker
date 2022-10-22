# Habit tracker app using pixela
# {'message': "Success. Let's visit https://pixe.la/@rajverma , it is your profile page!", 'isSuccess': True}

import os
import requests
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('username')
endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{endpoint}/{user}/graphs"
headers = {"X-USER-TOKEN": os.getenv('api_key')}
params = {"username": os.getenv('username'),
          "agreeTermsOfService": "yes",
          "notMinor": "yes"}

graph_coding = {"id": "graph1",
                "name": "coding-graph1",
                "unit": "commit",
                "type": "int",
                "color": "shibafu"}

graph_workout = {"id": "graph2",
                 "name": "workout-graph1",
                 "unit": "calories",
                 "type": "float",
                 "color": "ajisai"}


# for creating a new profile
def create_profile():
    response = requests.post(url=endpoint, json=params, headers=headers)
    response.raise_for_status()
    return response.json()


# post_data = requests.post(url=graph_endpoint, json=graph_workout, headers=headers)
# print(post_data.headers)
# print(post_data.text)

post_data = requests.post(url=f"{graph_endpoint}/{graph_workout['id']}",
                          headers=headers,
                          json={"date": "20221022", "quantity": "250"})

print(post_data.text)
