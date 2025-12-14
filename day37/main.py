import os
import requests
from datetime import datetime
#-----------USER----------------
github_username = os.environ.get("USERNAME")
pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = os.environ.get("PIXELA_TOKEN")
pixela_graph_id = "graph1"
# pixela_parameters = {
#     "token": pixela_token,
#     "username": github_username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

#-----------GRAPH----------------
graph_endpoint = f"{pixela_endpoint}/{github_username}/graphs"

graph_config = {
    "id": pixela_graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
    "timezone": "Asia/Manila",
}

headers = {
    "X-USER-TOKEN": pixela_token
}

#-----------PIXEL----------------
now = datetime(year=2025, month=12, day=6)

formatted_date = now.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{github_username}/graphs/{pixela_graph_id}/{formatted_date}"
pixel_config = {
    "quantity": "50",
}

response = requests.delete(url=pixel_endpoint, headers=headers)
print(response.text)