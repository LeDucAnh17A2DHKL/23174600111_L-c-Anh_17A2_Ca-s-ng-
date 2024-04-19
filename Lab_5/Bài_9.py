def can_convert(s1, s2):
    # Kiểm tra xem hai chuỗi có cùng độ dài hay không
    if len(s1) != len(s2):
        return False

    # Khởi tạo biến đếm số lượng ký tự khác nhau
    diff_count = 0

    for i in range(len(s1)):
        # Nếu hai ký tự không giống nhau, tăng biến đếm
        if s1[i] != s2[i]:
            diff_count += 1

        # Nếu có nhiều hơn một ký tự khác nhau, trả về False
        if diff_count > 1:
            return False

    # Nếu chỉ có một ký tự khác nhau, trả về True
    return diff_count == 1

# Gọi hàm
s1 = input("Nhập chuỗi thứ nhất: ")
s2 = input("Nhập chuỗi thứ hai: ")
print(can_convert(s1, s2))
