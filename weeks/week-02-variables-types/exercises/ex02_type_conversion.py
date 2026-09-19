"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả

print("cau 1: \n")
so_text = "42"
so = int(so_text)
so += 8
print("ket qua la: ",so)


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
print("\ncau 2: \n")
pi = 3.14159
sopi = int(pi)
print("ket qua khi chuyen qua int la: ",sopi)



# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("\ncau 3: \n")

print("ket qua cua bool(0)     la: ",bool(0))
print("ket qua cua bool(1)     la: ",bool(1))
print("ket qua cua bool("")    la: ",bool(""))
print("ket qua cua bool(hello) la: ",bool("hello"))
print("ket qua cua bool([])    la: ",bool([]))
print("ket qua cua bool([1,2]) la: ",bool([1, 2]))



# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
print("\ncau 4: \n")
chieucao = float(input("nhap chieu cao (m): "))
cannang = float(input("nhap can nang (kg): "))
bmi = cannang // (chieucao **2)
print(f"BMI cua ban la: {bmi:.1f}")


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
print("\ncau 5: \n")

giay = int(input("nhap so giay: "))

gio = giay // 3600
condu = giay % 3600

phut = condu // 60
giayconlai = condu % 60

print(gio, "gio",phut ,"phut",giayconlai,"giay")





