import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.boxplot(data = np.random.randn(100,4))
plt.title("Box plot")
plt.savefig("box plot")
plt.show()