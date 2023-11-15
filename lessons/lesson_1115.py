import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Step 1: Read data
heart_rate = []
with open('health.csv', 'r') as f:
    header = f.readline()  # read one line
    data = f.readlines()  # read all other lines

# print(header)
# print(data)

time = []
t = 0
for d in data:
    s1, s2, s3 = d.strip().split(',')  # remove \n, split by comma, assign to variables
    heart_rate.append([int(s1), int(s2), int(s3)])
    time.append(t)
    t += 1

# Step 2: Process data
mean = []
std = []
min = []
max = []
for v in heart_rate:
    mean.append(np.mean(v))
    std.append(np.std(v))
    min.append(np.min(v))
    max.append(np.max(v))

# Step 3: Graph
plt.errorbar(time, mean, std, fmt="+", color='#000000')
plt.xlabel("Time (hours)")
plt.ylabel("Heart Rate (BPM)")
plt.fill_between(time, max, min, alpha=0.25, linewidth=0, color="#303070")
plt.show()