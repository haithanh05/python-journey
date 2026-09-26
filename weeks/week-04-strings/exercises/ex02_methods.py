"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "

print("cau 1\n")
email = email.strip().lower()
print("email chuan hoa: ",email)

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"

print("cau 2\n")
print("title case: ",sentence.title())
print("dem so o: ",sentence.count("o"))
print("thay python: ",sentence.replace("python","PYTHON"))

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing

print("cau 3\n")
hoten = input("nhap ho ten day du: ")
parts = hoten.split()
print("ho: ",parts[0])
print("ten: ",parts[-1])


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()

print("cau 4\n")
tenf = input("nhap ten file: ")
if tenf.endswith(".py") or tenf.endswith(".txt") or tenf.endswith(".csv"):
    print("ten file hop le")
else:
    print("ten file khong hop le")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"

print("cau 5\n")
chuoi = input("nhap chuoi: ")
bước = int(input("nhap buoc: "))
kq = ""
for c in chuoi:
    kq += chr(ord(c) + bước)
print("chuoi sau khi ma hoa: ",kq)
