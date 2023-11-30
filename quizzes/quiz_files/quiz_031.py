from unit2_library import get_sensor
from matplotlib import pyplot as plt

# a). obtain temperature reading from sensor 1 and 2
sens_1 = get_sensor(id=1)
sens_2 = get_sensor(id=2)


# b). add the temperature values one by one
avg = []
time = []
t = 0
for n in range(len(sens_1)):
    temp = (sens_1[n] + sens_2[n])/2
    avg.append(temp)
    time.append(t)
    t += 5

# s3 = [a+b for a, b in zip(s1,s2)]

# c). create a graph with 3 subplots
plt.subplot(3,1,1)
plt.plot(time, sens_1)
plt.subplot(3,1,2)
plt.plot(time, sens_2)
plt.subplot(3,1,3)
plt.plot(time, avg)
plt.show()



