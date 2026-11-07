# groupby_concat.py
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['John', 'Jane', 'Jack', 'Jill'],
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 55000, 65000]
}
df = pd.DataFrame(data)

# Grouping by department and calculating average salary
# numeric_only=True skips text columns such as 'Name' (required in pandas >= 2.0)
grouped = df.groupby('Department').mean(numeric_only=True)
print("Average salary by department:")
print(grouped)

# Several aggregations on one column
summary = df.groupby('Department')['Salary'].agg(['count', 'mean', 'min', 'max'])
print("\nSalary summary by department:")
print(summary)

# Concatenating two DataFrames
data2 = {
    'Name': ['Jake', 'Laura'],
    'Department': ['HR', 'IT'],
    'Salary': [48000, 62000]
}
df2 = pd.DataFrame(data2)

df_concat = pd.concat([df, df2], ignore_index=True)
print("\nConcatenated DataFrame:")
print(df_concat)
