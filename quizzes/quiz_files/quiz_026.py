import matplotlib.pyplot as plt
import numpy as np

data = {
    'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    'y': [24, 1, 2, 25, 26, 21, 23, 34, 49, 2, 19, 32, 7, 17, 36, 7, 45, 28, 40, 46]
}

# Add title to dictionary
data["title"] = "quiz_data_science"

# Graph the data
plt.plot(data["x"], data["y"])
plt.title(data["title"], fontsize=15)
plt.show()