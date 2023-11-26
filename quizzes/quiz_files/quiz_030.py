import requests
from unit2_library import get_sensor, smoothing, coefficient
from matplotlib import pyplot as plt
import numpy as np

sensor2 = get_sensor(id=2)
x, y = smoothing(sensor2, size_window=5)
# x, y = smoothing(sensor2[200:400], size_window=5)
# t = x[200:400]
plt.plot(x,y)
plt.xlim(200,400)

#TODO: HL create a quadratic model for section
polyline = np.linspace(200,400,800)
line = np.poly1d(np.polyfit(x, y, 2)) #TODO: Polynomial for entire graph, for only section needed

print(np.polyfit(x, y, 2))

plt.plot(polyline,line(polyline))
plt.show()


# print(coefficient(x,y))
#
# (-0.02*x)**2)+(0.18*x)+20.2