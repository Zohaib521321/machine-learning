import pandas as pd
from faker import Faker
import numpy as np

# Initialize Faker
fake = Faker()

# Load the existing data from CSV
data = pd.read_csv("randomData.csv")

# print("Data is ",data.describe())



# # Generate a large amount of dummy data with some missing values
# dummy_data = pd.DataFrame({
#     'Name': [fake.name() if i%10!=0 else np.nan for i in range(1000)],  # Add missing names every 10th row
#     'Age': [fake.random_int(min=18, max=80) if i % 15 != 0 else np.nan for i in range(1000)],  # Add missing ages every 15th row
#     'City': [fake.city() if i % 20 != 0 else np.nan for i in range(1000)]  # Add missing cities every 20th row
# })

# # Concatenate the dummy data with the existing data
# merged_data = pd.concat([data, dummy_data], ignore_index=True)

# # Save the merged data back to the CSV file
# merged_data.to_csv("randomData.csv", index=False)

# # Apply filters as before (this will return rows with valid data in the columns used for filtering)
# filteredData = merged_data[merged_data['Age'] > 30]  # Automatically excludes NaN in Age
# filteredCity = merged_data[merged_data["City"] == "New York"]  # Automatically excludes NaN in City

# # Print the original and filtered data
# print("Data with missing values is: ")
# print(merged_data)

# print("\nNow the data after filtering by age (Age > 30):")
# print(filteredData)

# print("\nAfter filtering by city (City is 'New York'):")
# print(filteredCity)
