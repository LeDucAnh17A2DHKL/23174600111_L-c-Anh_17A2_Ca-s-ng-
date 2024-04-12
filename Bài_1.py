# Nhập số nguyên dương từ người dùng
n = int(input("Nhập một số nguyên dương: "))

# Kiểm tra xem n có phải là số nguyên dương không
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    # Chuyển đổi số nguyên dương thành nhị phân và in ra màn hình
    print(bin(n)[2:])
