import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Number of records
n_records = 100000

# Generate date range - spread bills across a realistic period
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = (end_date - start_date).days

# Generate random dates within the range for each record
random_days = np.random.randint(0, date_range, size=n_records)
dates = [start_date + timedelta(days=int(x)) for x in random_days]

# Generate synthetic data with normal distribution
consumer_ids = np.arange(1001, 1001 + n_records)
units_consumed = np.random.normal(loc=250, scale=50, size=n_records).clip(min=10)
rate_per_unit = np.random.normal(loc=5.5, scale=0.5, size=n_records).clip(min=3)
bill_amount = units_consumed * rate_per_unit + np.random.normal(loc=0, scale=10, size=n_records)
bill_amount = bill_amount.clip(min=50)

# Additional columns
meter_numbers = [f"MTR{i:06d}" for i in range(1, n_records + 1)]
customer_names = [f"Customer_{i}" for i in range(1, n_records + 1)]
payment_status = np.random.choice(['Paid', 'Pending', 'Overdue'], size=n_records, p=[0.7, 0.2, 0.1])

# Create DataFrame
df = pd.DataFrame({
    'Consumer_ID': consumer_ids,
    'Meter_Number': meter_numbers,
    'Customer_Name': customer_names,
    'Bill_Date': dates,
    'Units_Consumed': np.round(units_consumed, 2),
    'Rate_Per_Unit': np.round(rate_per_unit, 2),
    'Bill_Amount': np.round(bill_amount, 2),
    'Payment_Status': payment_status
})

# Save to CSV
df.to_csv('eb.csv', index=False)
print("Electricity bill dataset generated successfully!")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:\n{df.head()}")
print(f"\nStatistics:\n{df[['Units_Consumed', 'Bill_Amount']].describe()}")