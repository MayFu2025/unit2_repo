import numpy as np
import matplotlib.pyplot as plt

sensorA = [16,24,24,9,23,26,26,23,25]
sensorB = [2,19,25,10,11,24,17,7,24,17]
sensorC = [15,11,24,21,6,2,18,27,1,16]
time = []

t = 0
for n in range(len(sensorA)):
    time.append(t)
    t += 5

mean = []
std = []
min = []
max = []
for a in :
    mean.append(np.mean(v))
    std.append(np.std(v))
    min.append(np.min(v))
    max.append(np.max(v))