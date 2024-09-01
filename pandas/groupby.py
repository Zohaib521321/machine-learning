import pandas as pd

# Create a simple DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
# Group by 'Category' and calculate the mean of each group
grouped = df.groupby('Category').mean()

print("\nGrouped by 'Category' with mean values:")
print(grouped)

