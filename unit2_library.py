import requests

def get_sensor(id:int=1, ip:str="192.168.6.153"):
    request = requests.get(f"http://{ip}/readings")
    data = request.json()
    sensors = data['readings'][0]
    sensor = []
    for s in sensors:
        if s['sensor_id'] == id:
            sensor.append(s['value'])
    return sensor

def smoothing(x:list[int], size_window:int=5, overlap:float=1):
    smooth_x = []
    t = []
    for i in range(0,len(x), size_window):
        points = sum(x[i:(i+size_window)])/(size_window*overlap)
        smooth_x.append(points)
        t.append(i)

    return t, smooth_x

