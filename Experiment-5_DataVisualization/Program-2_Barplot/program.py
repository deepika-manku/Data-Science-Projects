import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'category':['A','B','C'],'values':[10,20,15]})
df.plot(kind = 'bar',x = 'category',y = 'values')
plt.title("Bar plot")
plt.savefig("Bar_plot")
plt.show()