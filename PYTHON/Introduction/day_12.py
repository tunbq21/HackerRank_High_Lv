import pandas as pd
import numpy as np

data = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Customer': ['An', 'Bình', 'Chi', 'An', 'Dũng', 'Bình', 'An', 'Chi'],
    'Product': ['iPhone 15', 'Samsung S23', 'Macbook', 'iPhone 15', 'iPad', 'Samsung S23', 'iPhone 15', 'Macbook'],
    'Quantity': [1, 2, '1', 3, 1, 1, np.nan, 2],
    'Price_Each': [1000, 800, 1500, 1000, 500, 800, 1000, 1500],
    'Order_Date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-05', '2023-01-07', '2023-01-08', '2023-01-10', '2023-01-12'],
    'Status': ['Shipped', 'Pending', 'Shipped', 'Shipped', 'Cancelled', 'Shipped', 'Shipped', np.nan]
}

df = pd.DataFrame(data)
print("Dữ liệu ban đầu:")
print(df.info())
print(df)


print("\n--- Xử lý dữ liệu ---")
df["Status"] = df["Status"].fillna("Unknown")
df["Quantity"] =df["Quantity"].fillna(0).astype(int)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df = df.drop_duplicates(subset=["Order_ID"], keep= False)
print(df)


df_3_columns = df[['Customer', 'Product', 'Price_Each']]
df_status_shipped = df[(df["Status"]== "Shipped") & (df["Price_Each"] > 1000)]
df_customer_an = df[df["Customer"] == "An"]

print("\n--- Dữ liệu sau khi lọc ---")
print(df_3_columns)
print(df_status_shipped)
print(df_customer_an)


df["Total_Sales"] = df["Quantity"] * df["Price_Each"]
df_Customer_Total_Sales = df.groupby("Customer")
df_Product_Quantity_Sold = df.groupby("Product")["Quantity"].sum()

summary = df.groupby('Product').agg({
    'Quantity': 'sum',
    'Total_Sales': ['mean', 'max']
})

print("\n--- Dữ liệu sau khi thêm cột Total_Sales ---")
print(df)
print("\n--- Tổng doanh thu theo từng khách hàng ---")
print(df_Customer_Total_Sales["Total_Sales"].sum())
print("\n--- Số lượng sản phẩm bán được theo từng loại ---")
print(df_Product_Quantity_Sold) 
print("\n--- Bảng tổng hợp theo sản phẩm ---")
print(summary)