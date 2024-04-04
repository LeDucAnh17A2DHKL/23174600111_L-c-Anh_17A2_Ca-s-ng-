# Định nghĩa các danh sách để lưu trữ các số lẻ và chẵn
odd_numbers = []
even_numbers = []

# Khởi tạo tổng
total = 0

# Định nghĩa một danh sách các số cho mục đích minh họa
numbers = [100, 200, 300, 400, 500]

# Lặp qua các số
for number in numbers:
    # Thêm số vào tổng
    total += number

    # Kiểm tra nếu tổng vượt quá 1000
    if total > 1000:
        break

    # Kiểm tra nếu số là lẻ hay chẵn và thêm nó vào danh sách tương ứng
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# In kết quả
print("a) Các số lẻ đã nhập:", odd_numbers)
print("b) Các số chẵn đã nhập:", even_numbers)
print("c) Đã nhập", len(odd_numbers) + len(even_numbers), "số nguyên.")
