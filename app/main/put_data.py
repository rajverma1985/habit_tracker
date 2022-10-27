import datetime
import os
import requests
from dotenv import load_dotenv

from dotenv import load_dotenv

load_dotenv()
user = os.getenv('username')
today = datetime.datetime.now()
update_date = datetime.datetime(year=2022, month=10, day=22)
endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{endpoint}/{user}/graphs"
headers = {"X-USER-TOKEN": os.getenv('api_key')}

graph_workout = {"id": "graph2",
                 "name": "workout-graph1",
                 "unit": "calories",
                 "type": "float",
                 "color": "ajisai"}

# do a PUT and DELETE
# update info and then delete as well, use the same endpoint but different params.
# https://pixe.la/v1/users/a-know/graphs/test-graph

new_workout_data = {"date": update_date.strftime("%Y%m%d"), "quantity": "250"}
update_endpoint = f"{graph_endpoint}/{graph_workout['id']}/{update_date.strftime('%Y%m%d')}"
response = requests.put(url=update_endpoint, json=new_workout_data, headers=headers)
print(update_endpoint)
print(response.text)
