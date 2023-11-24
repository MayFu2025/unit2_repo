# Bubble Sort
# Compare with neighbor, if neighbor is smaller then swap
x = [5, 6, 3, 2, 1, 4]
noChange = False

while not noChange:
    noChange= True  #Assume True
    for i in range(len(x)-1):  #The last number in list cannot be compared as there are no further values in list
        if x[i] > x[i+1]:
            temp = x[i]  #Temporary variable to store
            x[i] = x[i+1]
            x[i+1] = temp
            noChange = False  #If the code gets to this part (if statement), there was a change therefore noChange is False
print(x)

# Quiz 029
from matplotlib import pyplot as plt
from unit2_library import get_sensor, smoothing

# Test for Overlap:
x = [3, 2, 5, 7, 8, 9, 10, 11, 10, 11]
print(smoothing(x=x, size_window=4,overlap=0.5))

sensor2 = get_sensor(id=2)
x,y = smoothing(x=sensor2, size_window=4, overlap=0.5)
plt.subplot(2, 1, 1)
plt.plot(sensor2)
plt.subplot(2,1,2)
plt.plot(x,y)
plt.show()

# The function in unit2_library: added overlap parameter to function
# def smoothing(x:list[int], size_window:int=5, overlap:float=1):
#     smooth_x = []
#     t = []
#     for i in range(0,len(x), size_window):
#         points = sum(x[i:(i+size_window)])/(size_window*overlap)
#         smooth_x.append(points)
#         t.append(i)
#
#     return t, smooth_x