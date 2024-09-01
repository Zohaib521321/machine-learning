import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C', 'D'],
    'Value1': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'Key': ['B', 'D', 'E', 'F'],
    'Value2': [100, 200, 300, 400]
})

# Inner merge
inner_merged_df = pd.merge(df1, df2, on='Key')
print("Inner Merge (Default):")
print(inner_merged_df)

# Left join
left_join_df = pd.merge(df1, df2, on='Key', how='left')
print("\nLeft Join:")
print(left_join_df)

# Right join
right_join_df = pd.merge(df1, df2, on='Key', how='right')
print("\nRight Join:")
print(right_join_df)

# Outer join
outer_join_df = pd.merge(df1, df2, on='Key', how='outer')
print("\nOuter Join:")
print(outer_join_df)

# Merge on multiple columns
df1 = pd.DataFrame({
    'Key1': ['A', 'B', 'C', 'D'],
    'Key2': [1, 2, 3, 4],
    'Value1': [10, 20, 30, 40]
})

df2 = pd.DataFrame({
    'Key1': ['B', 'D', 'E', 'F'],
    'Key2': [2, 4, 5, 6],
    'Value2': [100, 200, 300, 400]
})

merged_df = pd.merge(df1, df2, on=['Key1', 'Key2'])
print("\nMerge on Multiple Columns:")
print(merged_df)

# Merge with suffixes
df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C'],
    'Value': [1, 2, 3]
})

df2 = pd.DataFrame({
    'Key': ['B', 'C', 'D'],
    'Value': [200, 300, 400]
})

merged_df = pd.merge(df1, df2, on='Key', suffixes=('_left', '_right'))
print("\nMerge with Suffixes:")
print(merged_df)
