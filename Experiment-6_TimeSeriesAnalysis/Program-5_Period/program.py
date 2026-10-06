#Create a monthly Period
import pandas as pd
p=pd.Period('2026-01', freq='M')
print("Original Period:", p)
#Convert monthly Period to daily frequency
daily_start=p.asfreq('D', how='start')
print("\nMonthly Period converted to Daily (Start):", daily_start)
daily_end=p.asfreq('D', how='end')
print("\nMonthly Period converted to Daily (End):", daily_end)
#Create a PeriodIndex
period_index=pd.period_range(start='2026-01',periods=3, freq='M')
print("\nOriginal PeriodIndex:", period_index)
#Convert PeriodIndex to daily frequency
daily_period_index=period_index.asfreq('D', how='start')
print("\nPeriodIndex converted to Daily Frequency:", daily_period_index)
#Convert PeriodIndex to daily frequency at end
daily_period_index_end=period_index.asfreq('D', how='end')
print("\nPeriodIndex converted to Daily Frequency (End):", daily_period_index_end)