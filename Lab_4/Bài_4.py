# Nhập vào từ bàn phím số nguyên n (n > 10)
n = int(input("Nhập vào từ bàn phím số nguyên n (n > 10): "))

# Khởi tạo biến cho các tổng
S1 = 0
S2 = 0
S3 = 0
S4 = 0
a = 1

# Tính toán các tổng sử dụng vòng lặp while
while a <= n:
    # Tính tổng S1
    S1 += 6

    # Tính tổng S2
    if a == 1:
        S2 = 1
    else:
        S2 += (a * (a + 1)) // 2

    # Tính tổng S3
    S3 += ((-1) ** a) * (a ** 2)

    # Tính tổng S4
    if a < 3:
        S4 += a * (a + 1) * (a + 2) // 6
    else:
        S4 += (n * (n + 1) * (n + 2)) // 6 - ( (n - a + 1) * (n - a + 2) * (n - a + 3) ) // 6

    a += 1

# In ra các tổng
print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"S3 = {S3}")
print(f"S4 = {S4}")