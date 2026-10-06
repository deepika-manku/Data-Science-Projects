import pandas as pd
#Create a Series with timestamp index
dates=pd.to_datetime(['2026-02-19', '2026-09-25', '2026-10-23'])
sales=pd.Series([1000, 2000, 3000], index=dates)
print("Original Series:")
print(sales)
#Convert Series from timestamps to monthly periods
period_series = sales.to_period('M')
print("\nSeries converted to Monthly Periods:")
print(period_series)
#Create a DataFrame with timestamp index
df = pd.DataFrame({'Sales': [1000, 2000, 3000],'Profit': [200, 300, 400]},index=dates)
print("\nOriginal DataFrame:")
print(df)
#Convert DataFrame to monthly periods
period_df = df.to_period('M')
print("\nDataFrame converted to Monthly Periods:")
print(period_df)