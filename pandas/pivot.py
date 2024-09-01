import pandas as pd

# Original DataFrame
df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [30, 75, 28, 77],
    'Humidity': [50, 20, 55, 25]
})

print("Original DataFrame:")
print(df)

# Pivot
pivot_df = df.pivot(index='Date', columns='City', values='Temperature')
print("\nPivot DataFrame:")
print(pivot_df)

# Melt
melted_df = df.melt(id_vars=['Date'], var_name='Metric', value_name='Value')
print("\nMelted DataFrame:")
print(melted_df)

# Melt with separation of city and metric
melted_df = df.melt(id_vars=['Date'], var_name='City_Metric', value_name='Value')
melted_df[['City', 'Metric']] = melted_df['City_Metric'].str.split('_', expand=True)
print("\nMelted DataFrame with City and Metric Columns:")
print(melted_df.drop(columns=['City_Metric']))
