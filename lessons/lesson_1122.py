# API part 1

import requests
import matplotlib.pyplot as plt
import numpy as np

x = {'usd':150, 'col':90}
for key,value in x.items():
    print(key, value)
for key in x.keys():
    print(key)
if 'eur' in x:
    print('eur')

## APIs ##

print("API stands for Application Programming Interface")
print("Every computer has an ip adress, which is like an address in the server")

ip_server = "192.168.6.153"

data = requests.get(f"http://{ip_server}/readings")
data = data.json() #Format data into json

x = data['readings'][0]
# print(x)
# print(f"There are {len(x)} readings in the server.")

my_sensors = {1:[], 2:[]} # Want to graph the two sensors
for record in x:
    id_sensor = record['sensor_id']
    if id_sensor in my_sensors:
        value = record['value']
        my_sensors[id_sensor].append(value)
# print(my_sensors)

# Create a graph
fig = plt.Figure(figsize=(10,8))
plt.subplot(2,1,1)  # row, column, id of currently editing graph
plt.plot(my_sensors[1], color="red")
plt.title("Outdoors Sensor")
plt.xlabel("Time (min)")
plt.ylabel("Temperature (C)")
plt.subplot(2,1,2)
plt.plot(my_sensors[2], color="blue")
plt.title("Indoors Sensor")
plt.xlabel("Time (min)")
plt.ylabel("Temperature (C)")
fig.tight_layout(pad=5.0)
plt.show()