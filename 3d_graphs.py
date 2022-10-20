from mpl_toolkits import mplot3d

import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('QtAgg')

fig = plt.figure()
ax = mplot3d.axes3d.Axes3D(fig)

z = np.linspace(0, 1, 100)
y = np.sin(z)
x = np.cos(z)

ax.scatter3D(x, y, z)
fig.show()
