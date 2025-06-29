import pandas as pd

# Load the Excel file
file_path = "ElectroGadget.xlsx"  # Make sure this file is in the same folder
df = pd.read_excel('https://github.com/shagunmishra02/analyze_data/blob/main/ElectroGadget.xlsx')

# Basic exploration
print("Shape of the dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values:\n", df.isnull().sum())
# Top 10 products by Units Sold
top_units = df.groupby('Product')['Units Sold'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Units Sold:")
print(top_units)

# Top 10 products by Revenue
top_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:")
print(top_revenue)
# Total Revenue by Region
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print("\nTotal Revenue by Region:")
print(region_revenue)

# Total Units Sold by Region
region_units = df.groupby('Region')['Units Sold'].sum().sort_values(ascending=False)
print("\nTotal Units Sold by Region:")
print(region_units)

# Most Sold Product per Region
most_sold_product_region = df.groupby(['Region', 'Product'])['Units Sold'].sum().reset_index()
most_sold_product_region = most_sold_product_region.sort_values(['Region', 'Units Sold'], ascending=[True, False])
top_products = most_sold_product_region.groupby('Region').first()
print("\nMost Sold Product per Region:")
print(top_products)
# Top 10 High-Value Transactions
top_transactions = df.sort_values(by='Revenue', ascending=False).head(10)
print("\nTop 10 High-Value Transactions:")
print(top_transactions[['OrderID', 'Product', 'Revenue', 'Region', 'SaleDate']])

# Revenue by Product
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print("\nRevenue by Product:")
print(product_revenue.head(10))  # Top 10 highest revenue generating products
