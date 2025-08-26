import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# --- Data Cleaning ---
df.dropna(subset=['Product Name'], inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# --- Analysis ---
monthly_sales = df.groupby(df['order_date'].dt.to_period("M"))['sales'].sum()
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(5)
region_sales = df.groupby('region')['sales'].sum()

# --- Visualizations ---
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.ylabel("Sales")
plt.savefig("monthly_sales.png")
plt.close()

plt.figure(figsize=(8,5))
top_products.plot(kind='bar', title='Top 5 Products by Revenue')
plt.ylabel("Revenue")
plt.savefig("top_products.png")
plt.close()

plt.figure(figsize=(6,6))
region_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales Share by Region')
plt.ylabel("")
plt.savefig("region_sales.png")
plt.close()

print("Analysis complete. Charts saved as PNG files.")
