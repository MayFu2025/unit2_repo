# Composite graphs

from unit2_library import get_sensor
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec

#step1 get sensors
sensors = []
for s in [0,1,2,3]:
    data = get_sensor(id=s)
    sensors.append(data)

num_samples = len(sensors[1])
average = []
for i in range(num_samples):
    total = 0
    for s in sensors:
        total += s[i]
    average.append(total/len(sensors))

#step2 plot data
fig = plt.figure(figsize=(10,8))
grid = GridSpec(3, 3, figure=fig, hspace=0.5)
# plt.subplots_adjust(hspace=0.5)

box_a = fig.add_subplot(grid[0:2, 0:2])  # grid(): Specify the range of grids it will take up
plt.plot(average, color="red")
plt.title("Average of all sensors")

box0 = fig.add_subplot(grid[0,2])  # Row, Column
plt.plot(sensors[0], color="blue")
plt.title("Sensor id=0")

box1 = fig.add_subplot(grid[1,2])
plt.plot(sensors[1], color="blue")
plt.title("Sensor id=1")

box2 = fig.add_subplot(grid[2,0])
plt.plot(sensors[2], color="blue")
plt.title("Sensor id=2")

box3 = fig.add_subplot(grid[2,1])
plt.plot(sensors[3], color="blue")
plt.title("Sensor id=3")

plt.show()