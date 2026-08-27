import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(50)
y=np.random.randn(50)
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("Scatter_Plot")
plt.show()