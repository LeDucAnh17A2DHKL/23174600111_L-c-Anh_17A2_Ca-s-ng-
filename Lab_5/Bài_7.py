def count_chars():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập chuỗi: ")

    # Khởi tạo bộ đếm
    lower, upper, digit, special = 0, 0, 0, 0

    for char in s:
        # Kiểm tra xem ký tự có phải là chữ cái viết thường, viết hoa, chữ số hay ký tự đặc biệt
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            digit += 1
        else:
            special += 1

    print(f"Chữ cái viết thường: {lower}")
    print(f"Chữ cái viết hoa: {upper}")
    print(f"Chữ số: {digit}")
    print(f"Ký tự đặc biệt: {special}")

# Gọi hàm
count_chars()
