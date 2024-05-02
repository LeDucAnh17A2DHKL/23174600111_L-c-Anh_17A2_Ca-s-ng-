# Yêu cầu nhập số nguyên N từ bàn phím
N = int(input("Hãy nhập một số nguyên N: "))

# Tạo một từ điển trống
dictionary_ten_sinh_vien = {}

# Thêm các phần tử vào từ điển
for i in range(1, N+1):
    dictionary_ten_sinh_vien[i] = i * 3

# In ra từ điển
print(dictionary_ten_sinh_vien)