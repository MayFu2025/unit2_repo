# Quiz 018
<hr>

### Prompt
![](images/quiz_018_slide.png)
*fig. 1* **Screenshot of quiz slides**

### Solution
```.py
def get_truth():
    out = "| A | B | C |\n"
    A = 0
    B = 0
    C = 0
    for n in range(8):
        out += f"| {int(A)} | {int(B)} | {int(C)} |\n"
        C = not(C)
        if (n+1) % 2 == 0:
            B = not(B)
        if (n+1) % 4 == 0:
            A = not(A)
    return out

# Check if it works:
print(get_truth())
```

### Evidence
![](images/quiz_018_evidence.png)
*fig. 2* **Screenshot of output in console**

### Boolean Logic Problem
![](images/quiz_018_bool.jpeg)
*fig. 3* **Working for given boolean logic problem**