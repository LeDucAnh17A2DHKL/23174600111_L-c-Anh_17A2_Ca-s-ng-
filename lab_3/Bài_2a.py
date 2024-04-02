# Khởi tạo biến tổng
tong = 0

# Duyệt qua các số trong khoảng từ 2000 đến 4000
for i in range(2000, 4001):
    # Kiểm tra nếu số đó chia hết cho 7 nhưng không chia hết cho 5
    if i % 7 == 0 and i % 5 != 0:
        # Cộng số đó vào biến tổng
        tong += i

# In ra kết quả
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000 là:", tong)
