import pandas as pd
import numpy as np
data=pd.Series(np.random.randn(6),index=[['a','a','b','b','c','c'],[1,2,1,2,1,2]])
df=data.unstack()
print(df)
print(df.stack())