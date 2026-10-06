import pandas as pd
dates=pd.to_datetime([
    '2026-02-19',
    '2026-06-15',
    '2026-08-06',
    '2026-08-24',
    '2026-09-25'
])
temperature=[26,30,29,31,28]
time_series=pd.Series(
    temperature,
    index=dates
)
print("Time Series:")
print(time_series)