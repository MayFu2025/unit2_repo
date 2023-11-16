import numpy as np
import matplotlib.pyplot as plt

sensorA = [16,24,24,9,23,26,26,23,25]
sensorB = [2,19,25,10,11,24,17,7,24,17]
sensorC = [15,11,24,21,6,2,18,27,1,16]

# Assuming time as the interval (Given in class)
time = []
t = 0
for n in range(len(sensorA)):
    time.append(t)
    t += 5

mean = []
std = []
min = []
max = []

for n in range(len(sensorA)):
    mean.append(np.mean([sensorA[n], sensorB[n], sensorC[n]]))
    std.append(np.std([sensorA[n], sensorB[n], sensorC[n]]))
    min.append(np.min([sensorA[n], sensorB[n], sensorC[n]]))
    max.append(np.max([sensorA[n], sensorB[n], sensorC[n]]))

plt.errorbar(time, mean, std, fmt="+", color='#000000')
plt.xlabel("Time")
plt.ylabel("Reading")
plt.fill_between(time, max, min, alpha=0.2, linewidth=0, color="#303030")
plt.title("May's Repository", fontsize=5, loc='right')
plt.show()
