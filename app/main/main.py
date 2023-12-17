# Habit tracker app using pixela
# {'message': "Success. Let's visit https://pixe.la/@rajverma , it is your profile page!", 'isSuccess': True}
import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('username')
today = datetime.datetime.now()
update_date = datetime.datetime(year=2022, month=10, day=22)
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
                 "unit": "minutes",
                 "type": "float",
                 "color": "ajisai"}

# coding_data = {"date": today.strftime("%Y%m%d"), "quantity": input("Please enter the number of commits:\n")}
workout_data = {"date": today.strftime("%Y%m%d"), "quantity": input("Please enter the workout minutes:\n")}


# for creating a new profile
def create_profile():
    response = requests.post(url=endpoint, json=params, headers=headers)
    response.raise_for_status()
    return response.json()


# for updating any graph "graph"> must have an ID key
def update_graph(graph):
    response = requests.put(url=f"{graph_endpoint}/{graph['id']}", headers=headers, json={"unit": graph['unit']})
    response.raise_for_status()
    return response.text


# for posting any data
def post_data(data):
    response = requests.post(url=f"{graph_endpoint}/{graph_workout['id']}", headers=headers, json=data)
    response.raise_for_status()
    return response.text


print(post_data(workout_data))
