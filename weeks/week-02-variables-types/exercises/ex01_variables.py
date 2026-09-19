"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = ???       (str)
# tuoi = ???      (int)
# diem_tb = ???   (float)
# dang_hoc = ???  (bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()
print("cau 1: \n")
ten : str = "Hai Thanh"
tuoi : int = 21
diem_tb : float = 9.0
dang_hoc : bool = True


print(ten,type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc,type(dang_hoc))




# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a

print("cau 2: \n")
a = 10
b = 20
a,b = b,a
print("a sau khi hoan doi la :", a)
print("b sau khi hoan doi la: ",b)



# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước

print("cau 3: ")
x = 100
print("gia tri khoi gan ban dau cho x la: ",x)
x +=10
print("gia tri cua x sau khi +10 la: ", x)
x -= 20
print("gia tri cua x sau khi -20 la: ", x)
x *=10
print("gia tri cua x sau khi *10: ", x)
x //=20
print("gia tri cua x sau khi //20 la: ",x)



# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
print("cau 4: \n")
ho, ten, tuoi = "Pham Nguyen", "Hai Thanh", 21
print("ho ten: ", ho,ten,tuoi,"tuoi")



