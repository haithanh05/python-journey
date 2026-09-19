"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
print("cau 1: ")

so1 = float(input("Nhap so thu nhat: "))
so2 = float(input("Nhap so thu hai: "))

tong = so1 + so2
hieu = so1 - so2
tich = so1 * so2
thuong = so1 / so2

print("Tong:", tong)
print("Hieu:", hieu)
print("Tich:", tich)
print("Thuong:", thuong)

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
print("cau 2: ")

r = float(input("Nhap ban kinh: "))

pi = 3.14159

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print("Dien tich:", dien_tich)
print("Chu vi:", chu_vi)

# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
print("cau 3: ")

gia_goc = float(input("Nhap gia goc: "))
phan_tram_giam = float(input("Nhap phan tram giam: "))

tien_giam = gia_goc * phan_tram_giam / 100
gia_sau_giam = gia_goc - tien_giam

print("Tien giam:", tien_giam)
print("Gia sau khi giam:", gia_sau_giam)

# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
print("cau 4: ")

tien_vnd = float(input("Nhap so tien VND: "))
ty_gia = float(input("Nhap ty gia USD/VND: "))

tien_usd = tien_vnd / ty_gia

print(f"So tien USD: {tien_usd:.2f} USD")

