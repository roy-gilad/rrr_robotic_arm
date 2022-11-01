import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,180,6)
y = (20,20,30,30,50,20)
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].grid()
axs[0].scatter(x, y)
axs[1].plot(x, y)


plt.show()