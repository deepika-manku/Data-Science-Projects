import pandas as pd
date_index=pd.date_range(
    start='2026-10-01',
    periods=4,
    freq='D'
)
print("Generated DatetimeIndex:")
print(date_index)