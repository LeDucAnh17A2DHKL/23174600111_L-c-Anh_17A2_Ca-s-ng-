# Khởi tạo một danh sách rỗng
numbers = []

# Nhận số phần tử từ người dùng
n = int(input("Nhập số lượng phần tử: "))

# Nhập các phần tử từ bàn phím
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    if num > 0:
        numbers.append(num)
    else:
        print("Vui lòng nhập một số nguyên dương.")
        i -= 1

# Khởi tạo biến even_sum và odd_sum
even_sum = 0
odd_sum = 0

# Phân loại và tính tổng các số chẵn và lẻ
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Xuất kết quả
print("\nTổng các số chẵn:", even_sum)
print("Tổng các số lẻ:", odd_sum)