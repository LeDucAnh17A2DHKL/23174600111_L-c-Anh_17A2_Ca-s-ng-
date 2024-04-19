def remove_spaces():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập chuỗi: ")

    # Xóa tất cả các khoảng trắng giữa các ký tự
    s_no_spaces = s.replace(" ", "")

    print(f"Chuỗi sau khi xóa khoảng trắng: {s_no_spaces}")

# Gọi hàm
remove_spaces()
