import pandas as pd
import numpy as np
df1=pd.DataFrame({'a':[1,np.nan,3],'b':[4,5,6]})
df2=pd.DataFrame({'a':[7,8,9],'b':[np.nan,11,12]})
merged=df1.combine_first(df2)
print(merged)