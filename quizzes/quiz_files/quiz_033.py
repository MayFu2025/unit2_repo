import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []

i = -4
while i<=4:
    y1.append(i**2)
    y2.append(-(i**2))
    x.append(i)
    i += 0.1

plt.figure(figsize=(8,8))
plt.plot(x,y1, color="red")
plt.plot(x,y2, color="black")
plt.plot(y1,x, color="brown")
plt.plot(y2,x, color="blue") #TODO: Make the plot labels show up?

plt.title("Four Parabolas Aligned with Axes")
plt.xlim(4,-4)
plt.ylim(4,-4)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()

plt.show()