# csv_read_write.py
from pathlib import Path

import pandas as pd

# Resolve paths next to this script so it works from any working directory
HERE = Path(__file__).resolve().parent
input_path = HERE / 'data.csv'
output_path = HERE / 'output.csv'

# Create a small sample file if data.csv is missing
if not input_path.exists():
    sample = pd.DataFrame({
        'Name': ['John', 'Jane', 'Jack', 'Jill'],
        'Age': [28, 34, 29, 41],
        'City': ['New York', 'London', 'Delhi', 'Sydney'],
        'Salary': [50000, 60000, 55000, 65000],
    })
    sample.to_csv(input_path, index=False)
    print(f"Created sample file: {input_path.name}")

# Reading a CSV file
df = pd.read_csv(input_path)
print("Data from CSV file:")
print(df)

# Writing to a CSV file (only people older than 30, as an example transformation)
df[df['Age'] > 30].to_csv(output_path, index=False)
print(f"\nRows with Age > 30 have been written to '{output_path.name}'.")
