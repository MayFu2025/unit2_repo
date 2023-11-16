# Quiz 022
<hr>

### Prompt
![](images/quiz_022_slide.png)
*fig. 1* **Screenshot of quiz slides**

### Solution
```.py
from matplotlib import pyplot as plt

x = []
y = []

i = -10
while i<=10:
    x.append(i)
    y.append(2*((i+5)**2))
    i += 0.2

plt.plot(x, y, marker='+') # Markers just to show that there are 100 points in the graph
plt.show()
```

### Evidence
![](images/quiz_022_evidence.png)
*fig. 2* **Screenshot of output graph**

### Boolean Logic Problem
![](images/quiz_022_bool.png)
*fig. 3* **Working for given boolean logic problem**