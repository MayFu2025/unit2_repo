from unit2_library import get_sensor
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec

sensor4 = get_sensor(4)
sensor5 = get_sensor(5)

both = []
for n in range(len(sensor4)):
    both.append(-(sensor4[n] + sensor5[n])/2)

fig = plt.figure(figsize=(10,5))
grid = GridSpec(3,4, figure=fig, hspace=0.5, wspace=0.2)

box_both = fig.add_subplot(grid[0:3,1:3])
plt.title("Sensor #4 - Sensor #5")
plt.plot(both, color='red')

box_4 = fig.add_subplot(grid[1,0])
plt.title("Sensor id = 4")
plt.ylim(0,100)
plt.xlim(0,800)
plt.plot(sensor4, color='black')

box_5 = fig.add_subplot(grid[1,3])
plt.title("Sensor id = 5")
plt.ylim(0,100)
plt.xlim(0,800)
plt.plot(sensor5, color='black')




plt.show()