"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# TODO 1: Cho ten = "An", tuoi = 20, diem = 8.567
# In ra: "Học sinh An, 20 tuổi, điểm TB: 8.57"
# Gợi ý: dùng :.2f để làm tròn 2 chữ số thập phân
ten = "An"
tuoi = 20
diem = 8.567

print("cau 1\n")
print("hoc sinh",ten,",",tuoi,"tuoi, diem TB: ",round(diem,2))


# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50

print("cau 2\n")
for i in range(1,11):
    print("5 x",i,"=",5*i)


# TODO 3: In hóa đơn mua hàng đẹp
# Dùng f-string để căn lề trái/phải
# ===========================
# SẢN PHẨM          GIÁ (VNĐ)
# ---------------------------
# Cà phê              35,000
# Bánh mì             25,000
# Nước suối            10,000
# ---------------------------
# TỔNG CỘNG           70,000
# ===========================
# Gợi ý: dùng f"{name:<20}{price:>10,}"

print("cau 3\n")
print("="*27)
print("SẢN PHẨM", "GIÁ (VNĐ)".rjust(20))
print("-"*27)
tong = 0
for i in range(3):
    ten_sp = input("nhap ten san pham: ")
gia = int(input("nhap gia: "))
print("-"*27)
print(ten_sp.ljust(20), gia)
tong += gia
print("-"*27)
print("TỔNG CỘNG", tong)
print("="*27)

# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%

print("cau 4\n")
pct = int(input("nhap phan tram: "))
print("[","█"*(pct//5),"░"*(20-pct//5), "]",pct,"%")
