import pandas as pd
import numpy as np
data=pd.Series(np.random.randn(6),index=[['a','a','b','b','c','c'],[1,2,1,2,1,2]])
print(data)
print(data['b'])
print(data[:,1])