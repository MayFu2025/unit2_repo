# Data science pt. 4(??)
from matplotlib import pyplot as plt
from unit2_library import get_sensor, smoothing

sensor1 = get_sensor()
x,y = smoothing(x=sensor1, size_window=5)
plt.subplot(2, 1, 1)
plt.plot(sensor1)
plt.subplot(2,1,2)
plt.plot(x, y)
plt.show()