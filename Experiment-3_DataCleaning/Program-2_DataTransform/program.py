import pandas as pd
import numpy as np
df=pd.DataFrame({'gender':['male','female','male']})
df['gender_num']=df['gender'].map({'male':0,'female':1})
df_renamed=df.rename(columns={'gender':'Gender'})
print(df_renamed)