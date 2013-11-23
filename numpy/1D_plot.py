import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 20)
y = np.linspace(0, 10, 20)

plt.plot(x, y) #line plot
plt.plot(x, y, 'o') #dot plot
plt.show()