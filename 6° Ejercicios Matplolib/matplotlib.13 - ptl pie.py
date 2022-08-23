import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Coconut"]
myexplode = [0.2, 0, 0, 0]


plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, startangle = 90)
plt.legend(title = "Four Fruits:")
plt.show() 