import serial

id = "cu.usbserial-110"
arduino = serial.Serial(port=f'/dev/{id}', baudrate=9600, timeout=1)  # Increase timeout if needed
print("Connection Successful")

def read():
    try:
        data = arduino.readline().decode('utf-8').strip()
        return data
    except UnicodeDecodeError as e:
        print(f"Error decoding data: {e}")
        return None

humidity = []
temperature = []

for i in range(100):
    msg = read()
    if msg is not None:
        print(msg)
        values = msg.split(',')
        if len(values) == 2:
            try:
                humidity.append(float(values[0]))
                temperature.append(float(values[1]))
            except ValueError as e:
                print(f"Error converting values to float: {e}")

arduino.close()