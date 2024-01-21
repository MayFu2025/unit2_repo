from matplotlib import pyplot as plt

x = []
y = []

i = 0
while i<=1:
    x.append(i)
    y.append(-i)
    i += 0.1

xp = []
yp = []
i = -1
while i<=1:
    xp.append(i)
    yp.append((i**2) + 1)


plt.plot(x,x, color="blue")
plt.plot(y,x, color="red")
plt.plot(xp,yp)
plt.show()