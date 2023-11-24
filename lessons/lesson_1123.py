# API part 2
import requests

user = {"username": "May", "password": "project2"}
ip = "192.168.6.153"

# Register User
# answer = requests.post(f'http://{ip}/register', json=user)
# print(answer.json())

# Log-in to get Cookie
answer = requests.post(f'http://{ip}/login', json=user)
print(answer.json())
cookie = answer.json()["access_token"]

# Put the cookie in the header of the request
header = {'Authorization':f'Bearer {cookie}'}

# Create a Sensor
# sensor_b = {
#     'type': 'temperature',
#     'location': 'Asama25',
#     'name': 'may_temp_1',
#     'unit': 'C'
# }
# answer = requests.post(f'http://{ip}/sensor/new', json=sensor_b, headers=header)
# print(answer.json())

# See your sensors + id
# answer = requests.get(f"http://{ip}/sensors", headers=header)
# print(answer.json())

# Send a recording to server
# record = {'sensor_id':23,'value':30}
# answer = requests.post(f'http://{ip}/sensor/reading/new', json=record, headers=header)
# print(answer.json())

# # Get all my recordings
# answer = requests.get(f"http://{ip}/user/readings", headers=header)
# print(answer.json())