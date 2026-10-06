import pandas as pd
dates=pd.date_range(start='2026-10-23 00:00', periods=3, freq='h')
values=[8, 9, 10]
time_series=pd.Series(values, index=dates)
print("Original Hourly Time Series:")
print(time_series)
#Resampling - calculate 3-hourly mean
resampled_series=time_series.resample('3h').mean()
print("\nResampled Time Series - 3 Hour Mean:")
print(resampled_series)
#Downsampling - Hourly to 4-hourly
downsampled_series=time_series.resample('4h').mean()
print("\nDownsampled Time Series - 4 Hour Mean:")
print(downsampled_series)
#Upsampling - Hourly to 30-minute intervals
upsampled_series=time_series.resample('30min').asfreq()
print("\nUpsampled Time Series - 30 Minute:")
print(upsampled_series)
#Upsampling with forward fill
upsampled_ffill=time_series.resample('30min').ffill()
print("\nUpsampled Time Series with Forward Fill:")
print(upsampled_ffill)