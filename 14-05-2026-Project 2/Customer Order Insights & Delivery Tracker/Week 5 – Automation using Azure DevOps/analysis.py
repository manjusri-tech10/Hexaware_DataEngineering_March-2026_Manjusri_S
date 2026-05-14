import pandas as pd
import numpy as np

df = pd.read_csv('orders.csv')
df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['issue'] = df['issue'].fillna('None')
df['delay_days'] = (df['delivery_date'] - df['order_date']).dt.days
df['delayed'] = np.where(df['delay_days'] > 5, 1, 0)

print("=== Delay Summary by Customer ===")
print(df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False))

print("\n=== Common Issues ===")
print(df[df['issue'] != 'None']['issue'].value_counts())

print("\nPipeline executed successfully.")