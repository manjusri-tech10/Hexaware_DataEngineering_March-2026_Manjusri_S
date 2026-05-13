import pandas as pd
import numpy as np

print("=== Supply Chain Pipeline Started ===")

# Load data
df = pd.read_csv("orders.csv")

# Process
df['delivery_date'] = pd.to_datetime(df['delivery_date'])
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['is_delayed'] = (df['delay_days'] > 0).astype(int)

# Summary
print(f"Total Orders: {len(df)}")
print(f"Delayed Orders: {df['is_delayed'].sum()}")
print(f"Average Delay Days: {df['delay_days'].mean():.2f}")
print(f"On-Time Orders: {(df['is_delayed'] == 0).sum()}")

# Save output log
df.to_csv("pipeline_output.csv", index=False)
print("Output saved to pipeline_output.csv")

print("=== Pipeline Completed Successfully ===")
