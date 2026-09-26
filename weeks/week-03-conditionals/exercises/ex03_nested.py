"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp

print("cau 1\n")

sodu = float(input("nhap so du: "))
rut = float(input("nhap so tien muon rut: "))
if rut > 0:
    if sodu >= rut:
        if rut % 50000 == 0:
            print("rut thanh cong")
            print(f"so du con lai: {sodu-rut}")
        else:
            print("rut sai")
    else:
        print("khong du tien")
else:
    print("rut sai")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ

print("cau 2\n")
cao = float(input("nhap chieu cao: "))
nang = float(input("nhap can nang: "))
bmi = nang / (cao * cao)
if bmi < 18.5:
    print("thieu can")
elif bmi >= 18.5 and bmi < 25:
    print("binh thuong")
elif bmi >= 25 and bmi < 30:
    print("thua can")
else:
    print("beo phi")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng

print("cau 3\n")
loai = input("nhap loai ve: ")
ngay = input("nhap ngay: ")
tuoi = int(input("nhap tuoi: "))
if loai == "vip":
    gia = 120000
else:
    gia = 80000

if ngay == "cuoi_tuan":
    gia = gia * 1.3
if tuoi < 12 or tuoi >= 65:
    gia = gia * 0.5
elif tuoi >= 18 and tuoi <= 25:
    gia = gia * 0.8

print("gia ve: ", int(gia))
