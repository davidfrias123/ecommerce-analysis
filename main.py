# Step 1 :Data load & preview
import pandas as pd
import os

# Set working directory
os.chdir(r"C:\Users\swath\Documents\ecommerce_project")

# Load CSV files
sales = pd.read_csv("sales_data"
".csv")
customers = pd.read_csv("customer_details.csv")
products = pd.read_csv("product_details.csv")

# Confirm successful loading
print("✅ Files loaded successfully!\n")
print("Sales shape:", sales.shape)
print("Customers shape:", customers.shape)
print("Products shape:", products.shape)

# Preview first few rows
print("\n--- Sales Data Preview ---")
print(sales.head())

print("\n--- Customer Data Preview ---")
print(customers.head())

print("\n--- Product Data Preview ---")
print(products.head())

# Step 2: Cleaning Data

# Clean column names for consistency
sales.columns = sales.columns.str.strip().str.lower().str.replace(' ', '_')
customers.columns = customers.columns.str.strip().str.lower().str.replace(' ', '_')
products.columns = products.columns.str.strip().str.lower().str.replace(' ', '_')

# Drop any unnecessary unnamed columns
sales = sales.loc[:, ~sales.columns.str.contains('unnamed')]
customers = customers.loc[:, ~customers.columns.str.contains('unnamed')]
products = products.loc[:, ~products.columns.str.contains('unnamed')]

# Fix typo in product id column
products.rename(columns={'uniqe_id': 'product_id'}, inplace=True)

print("\n✅ Columns cleaned successfully!")
print("Sales columns:", sales.columns.tolist())
print("Customers columns:", customers.columns.tolist())
print("Products columns:", products.columns.tolist())

# Step 3: Merging Datasets

merged_df = (
    sales
    .merge(customers, how='left', left_on='user_id', right_on='customer_id')
    .merge(products, how='left', on='product_id')
)

print("\n✅ Merging completed!")
print("Merged dataset shape:", merged_df.shape)
print(merged_df.head())

# Step 4: Save Merged Data
merged_df.to_csv("merged_ecommerce_data.csv", index=False)
print("\n💾 Saved as merged_ecommerce_data.csv")

# step 5: open and preview merged data
merged_df = pd.read_csv("merged_ecommerce_data.csv")
print("\n--- Merged Data Preview ---")
print(merged_df.head(10))
