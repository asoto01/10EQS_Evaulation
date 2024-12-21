import sys
import csv
import pandas as pd

# Load the datasets
synthetic_data = pd.read_csv("synthetic_products_enhanced.csv")

# Accessing the CSV file path
csv_file_path = sys.argv[1]
base_data = pd.read_csv(csv_file_path)

# Merge data on product_name
merged_data = pd.merge(base_data, synthetic_data, on="product_name", how="outer", suffixes=('_base', '_synthetic'))

# Analyze average price by category
average_prices = merged_data.groupby('category_base')[['our_price_base', 'our_price_synthetic']].mean()

# Identify price differences for the same product
merged_data['price_difference'] = merged_data['our_price_synthetic'] - merged_data['our_price_base']

# Summary of significant price differences
significant_differences = merged_data[merged_data['price_difference'].abs() > 2]  # Customize threshold

print("Average Prices by Category:")
print(average_prices)
print("\nSignificant Price Differences:")
print(significant_differences)
