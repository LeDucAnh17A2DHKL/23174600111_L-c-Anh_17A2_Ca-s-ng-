# Khởi tạo biến tổng
tong = 0

# Duyệt qua các số trong khoảng từ 500 đến 1000
for i in range(500, 1001):
    # Kiểm tra nếu số đó chia hết cho 4 nhưng không chia hết cho 6
    if i % 4 == 0 and i % 6 != 0:
        # Cộng số đó vào biến tổng
        tong += i

# In ra kết quả
print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000 là:", tong)
