def special_char_percentage():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập chuỗi: ")

    # Khởi tạo từ điển để lưu trữ ký tự đặc biệt và số lần xuất hiện
    special_chars = {}

    for char in s:
        # Kiểm tra xem ký tự có phải là ký tự đặc biệt không
        if not char.isalnum():
            # Nếu có, tăng số lần xuất hiện của ký tự đặc biệt
            special_chars[char] = special_chars.get(char, 0) + 1

    total_chars = len(s)
    print("Ký tự đặc biệt và tỷ lệ phần trăm:")

    for char, count in special_chars.items():
        # Tính tỷ lệ phần trăm của mỗi ký tự đặc biệt
        percentage = (count / total_chars) * 100
        print(f"'{char}': {count} lần, chiếm {percentage:.2f}%")

# Gọi hàm
special_char_percentage()
