"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
print("ky tu dau: ",s[0])
print("ky tu cuoi: ",s[-1])
print("5 ky tu dau: ",s[:5])


# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s

print("cau 2\n")
print("Journey: ",s[7:])
print("dao nguoc: ",s[::-1])
print("lay moi ky tu thu 2: ",s[::2])


# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099

print("cau 3\n")
cccd = input("nhap cccd: ")
print("ma tinh: ",cccd[:2])
print("gioi tinh: ",cccd[2])
print("nam sinh: ",cccd[3:5])


# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]

print("cau 4\n")
s = input("nhap chuoi: ")
if s == s[::-1]:
    print("chuoi doi xung")
else:
    print("chuoi khong doi xung")
