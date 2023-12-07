# listening_arduino
import serial
from pyfirmata import Arduino
import time

id = "cu.usbserial-110"
arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=0.1)
print("Connection Successful")


def read():
    data = ""
    while len(data) < 1:
        data = arduino.readline()
    return data.decode('utf-8')  #utf-8 is the same as ascii

humidity = []
temperature = []
for i in range(5):
    msg = read()
    print(msg)
    time.sleep(1)
#     hum = msg.split(' ')[0]
#     temp = msg.split(' ')[1]
#     hum = (hum.split(':'))[1].strip('%')
#     temp = (temp.split(':'))[1].strip('C')
#     humidity.append(hum)
#     temperature.append(temp)
# print(humidity)
# print(temperature)

#TODO: Make graph
# Humidity:20.00% Temperature:23.80C
