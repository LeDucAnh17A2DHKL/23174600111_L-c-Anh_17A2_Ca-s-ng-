# Khởi tạo hai số đầu tiên của dãy Fibonacci
a, b = 0, 1

# In ra hai số đầu tiên
print(a, b, end=" ")

# Tính toán và in ra các phần tử tiếp theo trong dãy Fibonacci cho đến khi phần tử tiếp theo lớn hơn hoặc bằng 100
while True:
    c = a + b
    
    if c >= 100: # Kiểm tra điều kiện
        break
    
    print(c, end=" ")
    
    # Cập nhật giá trị của a và b để tính toán phần tử tiếp theo
    a = b
    b = c
