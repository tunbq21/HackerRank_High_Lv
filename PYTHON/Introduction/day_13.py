import pandas as pd
import numpy as np

data = {
    'Property_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Location': [' District 2 ', 'District 3', ' District 1', 'District 2', 'District 3', 'District 1', 'District 2', 'District 1'],
    'Type': ['Apartment', 'House', 'Apartment', 'Villa', 'House', 'Apartment', 'Villa', 'Apartment'],
    'Price_USD': ['150000', '280000', '135000', '500000', '275000', '160000', 'nan', '140000'],
    'Area_m2': [55, 120, 50, 250, 115, 60, 230, 52],
    'Bedrooms': [1, 3, 1, 4, 3, 2, 4, 1],
    'Year_Built': [2015, 2010, 2018, 2020, 2010, 2015, 2021, 2018]
}

df_house = pd.DataFrame(data)
print("Dữ liệu Bất động sản:")
print(df_house)


print("\n--- Xử lý dữ liệu ---")
df_house["Location"] = df_house['Location'].str.strip()

df_house["Price_USD"] = pd.to_numeric(df_house['Price_USD'], errors='coerce')

df_house_lowt_15 = df_house[(df_house["Price_USD"] < 150000) & (df_house["Location"] == "District 1")]

df_house_m2_50_60 = df_house[(df_house["Area_m2"].between(50, 60))]

df_house_apartment = df_house[(df_house["Area_m2"].between(50, 60)) & (df_house["Type"] == "Apartment")]

df_house_built_lowt_2018 = df_house[(df_house["Year_Built"] < 2018)]

df_house_morethan_2018 = df_house[df_house["Year_Built"] > 2018] 

# print("\n--- Dữ liệu sau khi lọc ---")
# print(df_house_lowt_15)
# print(df_house_m2_50_60)
# print(df_house_apartment)
# print(df_house_built_lowt_2018)
# print(df_house_morethan_2018)



agg_result = df_house.groupby('Type').agg(
    {
        'Price_USD': 'mean', 
        'Area_m2': 'sum'
        }
    ).reset_index()


df_house_max_price_Location = df_house.groupby("Location").agg({"Price_USD": "max"}).reset_index()

count_loc_type = df_house.groupby(['Location', 'Type']).size()


print(df_house.dtypes)
print("\n--- Tổng diện tích và giá trung bình theo loại nhà ---")
print(agg_result)
print("\n--- Giá cao nhất theo từng khu vực ---")
print(df_house_max_price_Location)

print("\n--- Số lượng nhà theo từng khu vực và loại ---")
print(count_loc_type)


df_house['Price_per_m2'] = df_house['Price_USD'] / df_house['Area_m2']

mean_price = df_house['Price_USD'].mean()
df_house['Price_USD'] = df_house['Price_USD'].fillna(mean_price)

df_house['Segment'] = np.where(df_house['Price_USD'] > 300000, 'Luxury', 'Standard')

print(df_house)

print("\n--- Dữ liệu sau khi thêm cột Price_per_m2 và xử lý giá trị thiếu ---")
print(df_house)

df_house["Age"] = 2026 - df_house["Year_Built"]
print("\n--- Dữ liệu sau khi thêm cột Age ---")
print(df_house)

conditions = [
    (df_house['Age'] <= 5),
    (df_house['Age'] > 5) & (df_house['Age'] <= 10),
    (df_house['Age'] > 10)

]
segments = ['New', 'Moderate', 'Old']
df_house["Renovation_Urgency"] = np.select(conditions, segments, default='Unknown')
print("\n--- Dữ liệu sau khi thêm cột Renovation_Urgency ---")
print(df_house)

# 1. Lọc theo danh sách ưu tiên
priority_districts = ['District 1', 'District 3']
df_priority = df_house[df_house['Location'].isin(priority_districts)]

# 2. Lọc Type KHÔNG chứa chữ 'Villa'
# Dùng ~ để lấy các giá trị False từ hàm str.contains
df_no_villa = df_house[~df_house['Type'].str.contains('Villa')]

# 1. Tìm BĐS có diện tích > 2 lần diện tích trung bình
mean_area = df_house['Area_m2'].mean()
outliers_area = df_house[df_house['Area_m2'] > (2 * mean_area)]

# 2. Tìm Location có tổng giá trị BĐS lớn nhất
# idxmax() trả về nhãn (Location) của giá trị lớn nhất sau khi sum
top_location = df_house.groupby('Location')['Price_USD'].sum().idxmax()
print(f"Khu vực có tổng giá trị cao nhất: {top_location}")

# 3. Xuất ra file CSV
df_house.to_csv('cleaned_housing_data.csv', index=False)


# ========================================================================

# Khởi tạo dữ liệu chủ sở hữu
owners_data = {
    'Property_ID': [1, 3, 4, 5, 9],
    'Owner_Name': ['An', 'Bình', 'Chi', 'Dũng', 'Hạnh'],
    'Owner_Phone': ['0901', '0902', '0903', '0904', '0905']
}
df_owners = pd.DataFrame(owners_data)

# 1. Inner Join: Chỉ lấy những căn có chủ sở hữu
# df_inner = pd.merge(df_house, df_owners, on='Property_ID', how='inner')
df_inner = pd.merge(df_house, df_owners, left_on='Property_ID', right_on='Property_ID', how='inner')

# 2. Left Join: Giữ toàn bộ danh sách nhà, thiếu chủ thì để NaN
df_final = pd.merge(df_house, df_owners, on='Property_ID', how='left')

# 3. Kiểm tra số căn trống thông tin chủ sở hữu
missing_owners = df_final['Owner_Name'].isna().sum()
print(f"Số căn chưa có chủ sở hữu: {missing_owners}")

# 1. Ranking: Xếp hạng giá theo từng khu vực
# method='dense' giúp các hạng không bị nhảy số nếu có giá bằng nhau
df_house['Price_Rank'] = df_house.groupby('Location')['Price_USD'].rank(ascending=False, method='dense')

# 2. Correlation: Tính tương quan giữa diện tích và giá
# Kết quả gần 1: Tỷ lệ thuận mạnh | Gần 0: Không liên quan | Gần -1: Tỷ lệ nghịch
correlation = df_house['Area_m2'].corr(df_house['Price_USD'])
print(f"Độ tương quan giữa Diện tích và Giá: {correlation:.2f}")

# 3. Lọc Top 3 bất động sản giá cao nhất
top_3_expensive = df_house.nlargest(3, 'Price_USD')