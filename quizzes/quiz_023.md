# Quiz 023
<hr>

### Prompt
![](images/quiz_023_slide.png)
*fig. 1* **Screenshot of quiz slides**

### Solution
```.py
from matplotlib import pyplot as plt

x = []
y = []

i = -10
while i<=10:
    x.append(i)
    y.append(abs(i))
    i += 0.2

plt.plot(x, y, marker='+') # Markers just to show that there are 100 points in the graph
plt.show()
```

### Evidence
![](images/quiz_001_evidence.png)
*fig. 2* **Screenshot of output graph**

### Boolean Logic Problem
![](images/quiz_001_bool.png)
*fig. 3* **Working for given boolean logic problem**