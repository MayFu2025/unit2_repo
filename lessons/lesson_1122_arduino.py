# listening_arduino

import serial
from pyfirmata import Arduino

id = "cu.usbserial-110"
arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=0.1)
print("Connection Successful")


def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data.decode('utf-8')  #utf-8 is the same as ascii


data = """
Humidity:35.00% Temperature:18.50C
Humidity:35.00% Temperature:18.50C
Humidity:36.30% Temperature:18.60C
Humidity:36.30% Temperature:18.60C
Humidity:36.60% Temperature:18.70C
Humidity:36.60% Temperature:18.70C
Humidity:36.60% Temperature:18.80C
Humidity:36.60% Temperature:18.80C
Humidity:36.80% Temperature:18.90C
Humidity:36.80% Temperature:18.90C
Humidity:36.90% Temperature:19.00C
Humidity:36.90% Temperature:19.00C
Humidity:37.00% Temperature:19.00C
Humidity:37.00% Temperature:19.00C
Humidity:36.80% Temperature:19.10C
Humidity:36.80% Temperature:19.10C
Humidity:36.40% Temperature:19.20C
Humidity:36.40% Temperature:19.20C
Humidity:36.10% Temperature:19.20C
Humidity:36.10% Temperature:19.20C
Humidity:35.90% Temperature:19.30C
Humidity:35.90% Temperature:19.30C
Humidity:35.80% Temperature:19.30C
Humidity:35.80% Temperature:19.30C
Humidity:35.60% Temperature:19.40C
Humidity:35.60% Temperature:19.40C
Humidity:35.50% Temperature:19.40C
Humidity:35.50% Temperature:19.40C
Humidity:35.50% Temperature:19.50C
Humidity:35.50% Temperature:19.50C
Humidity:35.30% Temperature:19.50C
Humidity:35.30% Temperature:19.50C
Humidity:35.10% Temperature:19.60C
Humidity:35.10% Temperature:19.60C
Humidity:35.10% Temperature:19.60C
Humidity:35.10% Temperature:19.60C
Humidity:35.00% Temperature:19.60C
Humidity:35.00% Temperature:19.60C
Humidity:34.90% Temperature:19.70C
Humidity:34.90% Temperature:19.70C
Humidity:34.60% Temperature:19.80C
Humidity:34.60% Temperature:19.80C
Humidity:34.50% Temperature:19.80C
Humidity:34.50% Temperature:19.80C
Humidity:34.40% Temperature:19.80C
Humidity:34.40% Temperature:19.80C
Humidity:34.30% Temperature:19.90C
Humidity:34.30% Temperature:19.90C
Humidity:34.20% Temperature:19.90C
Humidity:34.20% Temperature:19.90C
Humidity:34.10% Temperature:19.90C
Humidity:34.10% Temperature:19.90C
Humidity:34.10% Temperature:20.00C
Humidity:34.10% Temperature:20.00C
Humidity:34.00% Temperature:20.00C

Humidity:34.00% Temperature:20.00C

Humidity:34.00% Temperature:20.00C

Humidity:34.00% Temperature:20.00C

Humidity:33.80% Temperature:20.10C

Humidity:33.80% Temperature:20.10C

Humidity:33.70% Temperature:20.10C

Humidity:33.70% Temperature:20.10C

Humidity:33.70% Temperature:20.10C

Humidity:33.70% Temperature:20.10C

Humidity:33.60% Temperature:20.20C

Humidity:33.60% Temperature:20.20C

Humidity:33.80% Temperature:20.20C

Humidity:33.80% Temperature:20.20C

Humidity:33.80% Temperature:20.20C

Humidity:33.80% Temperature:20.20C

Humidity:33.60% Temperature:20.30C

Humidity:33.60% Temperature:20.30C

Humidity:33.50% Temperature:20.30C

Humidity:33.50% Temperature:20.30C

Humidity:33.40% Temperature:20.30C

Humidity:33.40% Temperature:20.30C

Humidity:33.40% Temperature:20.30C
Humidity:33.40% Temperature:20.30C
Humidity:33.30% Temperature:20.40C
Humidity:33.30% Temperature:20.40C
Humidity:33.30% Temperature:20.40C
Humidity:33.30% Temperature:20.40C
Humidity:33.20% Temperature:20.40C
Humidity:33.20% Temperature:20.40C
Humidity:33.20% Temperature:20.50C
Humidity:33.20% Temperature:20.50C
Humidity:33.20% Temperature:20.50C
Humidity:33.20% Temperature:20.50C
Humidity:33.20% Temperature:20.50C
Humidity:33.20% Temperature:20.50C
Humidity:33.00% Temperature:20.60C
Humidity:33.00% Temperature:20.60C
Humidity:32.90% Temperature:20.60C
Humidity:32.90% Temperature:20.60C
Humidity:32.80% Temperature:20.60C
Humidity:32.80% Temperature:20.60C
Humidity:32.70% Temperature:20.60C
Humidity:32.70% Temperature:20.60C
Humidity:32.70% Temperature:20.70C
"""

humidity = []
temperature = []
for i in range(100):
    msg = read()
    print(msg)
    hum = msg.split(' ')[0]
    temp = msg.split(' ')[1]
    hum = (hum.split(':'))[1].strip('%')
    temp = (temp.split(':'))[1].strip('C')
    humidity.append(hum)
    temperature.append(temp)
print(humidity)
print(temperature)

#TODO: Make graph
# Humidity:20.00% Temperature:23.80C
