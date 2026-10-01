import pandas as pd 

file_path="Data/online+retail/online_retail.xlsx"
df= pd.read_excel(file_path)

# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.info())

# print(df.isnull().sum())
# print(df.duplicated().sum())
# df = df.drop_duplicates()

# print("New shape:", df.shape)
# print(df[df["CustomerID"].isnull()].head())
# print(df[df["Description"].isnull()].head())
#print(df[df["Description"].isnull()][["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]].head(10))
# print((df["UnitPrice"] == 0).sum())
#print(df[df["UnitPrice"] == 0][["InvoiceNo", "StockCode", "Description", "Quantity"]].head(10))
zero_price = df[df["UnitPrice"] == 0]

# print("Positive quantity:", (zero_price["Quantity"] > 0).sum())
# print("Negative quantity:", (zero_price["Quantity"] < 0).sum())
# print("Zero quantity:", (zero_price["Quantity"] == 0).sum())
# print(df["InvoiceNo"].astype(str).str.startswith("C").sum())
c_invoices = df[df["InvoiceNo"].astype(str).str.startswith("C")]

# print(c_invoices["Quantity"].head(10))
# print(c_invoices["Quantity"].sum())
# print(c_invoices["Quantity"].abs().sum())
# print((df["Quantity"] < 0).sum())
negative_qty = df[df["Quantity"] < 0]

# print(negative_qty[~negative_qty["InvoiceNo"].astype(str).str.startswith("C")].head(10))
#print(negative_qty[~negative_qty["InvoiceNo"].astype(str).str.startswith("C")]["StockCode"].value_counts().head(10))
#print(df["InvoiceNo"].astype(str).str.len().value_counts())
# print(df[
#     (df["InvoiceNo"].astype(str).str.len() == 7) &
#     (~df["InvoiceNo"].astype(str).str.startswith("C"))
# ][["InvoiceNo", "Quantity", "UnitPrice"]])
#print(df["InvoiceNo"].astype(str).str.startswith("A").sum())
#print((df["UnitPrice"] < 0).sum())
#
#print(df[df["UnitPrice"] < 0][["InvoiceNo", "StockCode", "Description", "Quantity", "UnitPrice"]])
sales_df = df[
    (~df["InvoiceNo"].astype(str).str.startswith("C")) &
    (df["UnitPrice"] >= 0)
]

# print(sales_df.shape)
# print((sales_df["Quantity"] == 0).sum())
# print((sales_df["Quantity"] < 0).sum())
negative_sales = sales_df[sales_df["Quantity"] < 0]

# print(negative_sales[[
#     "InvoiceNo",
#     "StockCode",
#     "Description",
#     "Quantity",
#     "UnitPrice"
# ]].head(10))
# print((negative_sales["UnitPrice"] == 0).sum())
sales_df = sales_df[sales_df["Quantity"] > 0]

# print("Final shape:", sales_df.shape)
sales_df["Revenue"] = sales_df["Quantity"] * sales_df["UnitPrice"]

# print(sales_df[["Quantity", "UnitPrice", "Revenue"]].head())
# total_revenue = sales_df["Revenue"].sum()

# print("Total Revenue:", total_revenue)
sales_df["InvoiceDate"] = pd.to_datetime(sales_df["InvoiceDate"])

# print(sales_df["InvoiceDate"].dtype)
sales_df["Month"] = sales_df["InvoiceDate"].dt.to_period("M")

# print(sales_df[["InvoiceDate", "Month"]].head())
monthly_revenue = sales_df.groupby("Month")["Revenue"].sum()

# print(monthly_revenue)
top_products = sales_df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

# print(top_products)
top_revenue_products = (
     sales_df.groupby("Description")["Revenue"]
     .sum()
     .sort_values(ascending=False)
     .head(10)
 )

# print(top_revenue_products)
# print(
#     sales_df[sales_df["Description"].isin(["DOTCOM POSTAGE", "Manual", "POSTAGE"])]
#     [["StockCode", "Description"]]
#     .drop_duplicates()
# )
product_sales = sales_df[
    ~sales_df["StockCode"].isin(["POST", "DOT", "M", "m"])
]

# print(product_sales.shape)
# top_product_revenue = (
#     product_sales.groupby("Description")["Revenue"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# print(top_product_revenue)
country_revenue = (
    sales_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# print(country_revenue.head(10))
customer_revenue = (
     sales_df.dropna(subset=["CustomerID"])
     .groupby("CustomerID")["Revenue"]
     .sum()
     .sort_values(ascending=False)
     .head(10)
 )

# print(customer_revenue)
# customer_orders = (
#     sales_df.dropna(subset=["CustomerID"])
#     .groupby("CustomerID")["InvoiceNo"]
#     .nunique()
# )

# repeat_customers = (customer_orders > 1).sum()
# one_time_customers = (customer_orders == 1).sum()

# print("Repeat Customers:", repeat_customers)
# print("One-time Customers:", one_time_customers)
# order_revenue = sales_df.groupby("InvoiceNo")["Revenue"].sum()

# average_order_value = order_revenue.mean()

# print("Average Order Value:", average_order_value)
# cancelled_orders = df[
#     df["InvoiceNo"].astype(str).str.startswith("C")
# ]

# print("Cancelled Orders:", cancelled_orders["InvoiceNo"].nunique())
# print("Cancelled Quantity:", abs(cancelled_orders["Quantity"].sum()))
# country_orders = (
#     sales_df.groupby("Country")["InvoiceNo"]
#     .nunique()
#     .sort_values(ascending=False)
#     .head(10)
# )

# print(country_orders)
# pehle wala code...
monthly_revenue = (
    sales_df.groupby("Month")["Revenue"].sum()
)

# chart wala code
import matplotlib.pyplot as plt

#plt.figure(figsize=(10, 5))

# monthly_revenue.plot(kind="line", marker="o")

# plt.title("Monthly Revenue Trend")
# plt.xlabel("Month")
# plt.ylabel("Revenue (£)")
# plt.xticks(rotation=45)
# plt.grid(True)

# plt.tight_layout()
# plt.savefig("monthly_revenue.png")
# plt.show()
# plt.figure(figsize=(10, 6))

# top_revenue_products.sort_values().plot(kind="barh")

# plt.title("Top 10 Products by Revenue")
# plt.xlabel("Revenue (£)")
# plt.ylabel("Product")

# plt.tight_layout()
# plt.savefig("top_10_products_revenue.png")
# plt.show()
# plt.figure(figsize=(10, 6))

# country_revenue.head(10).sort_values().plot(kind="barh")

# plt.title("Top 10 Countries by Revenue")
# plt.xlabel("Revenue (£)")
# plt.ylabel("Country")

# plt.tight_layout()
# plt.savefig("top_10_countries_revenue.png")
# plt.show()
plt.figure(figsize=(10, 6))

customer_revenue.sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Customer ID")

plt.tight_layout()
plt.savefig("top_10_customers_revenue.png")
plt.show()






