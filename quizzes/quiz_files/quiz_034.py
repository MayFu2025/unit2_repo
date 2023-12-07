# Four Funny Parabolas
from matplotlib import pyplot as plt

x1 = []
x2 = []
y1 = []
y2 = []

i = -10
while i<=0:
    x1.append(i)
    x2.append(-i)
    y1.append((i+2)**2)
    y2.append(-((i + 2) ** 2))
    i += 0.1

plt.figure(figsize=(8,8))
plt.plot(x1,y1, color="red")
plt.legend("Parabola 1")
plt.plot(x1,y2, color="blue")
plt.legend("Parabola 3")
plt.plot(x2,y1, color="black")
plt.legend("Parabola 2")
plt.plot(x2,y2, color="brown")
plt.legend("Parabola 4")

plt.xlim(-15,15)
plt.ylim(-15,15)
plt.title("Four Funny Parabolas")
plt.show()