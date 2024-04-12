def manipulate_string():
    # Nhập chuỗi từ bàn phím
    s = input("Nhập chuỗi: ")

    # a) Trích xuất các ký tự từ vị trí thứ 2 đến vị trí thứ 8
    extracted_a = s[1:8]
    print(f"a) Chuỗi từ vị trí thứ 2 đến vị trí thứ 8: {extracted_a}")

    # b) Trích xuất một chuỗi con chứa 5 ký tự cuối cùng
    extracted_b = s[-5:]
    print(f"b) Chuỗi 5 ký tự cuối cùng: {extracted_b}")

    # c) Trích xuất một chuỗi con chứa 3 ký tự cuối cùng
    extracted_c = s[-3:]
    print(f"c) Chuỗi 3 ký tự cuối cùng: {extracted_c}")

    # d) Chuyển đổi tất cả các chữ cái viết thường trong chuỗi thành chữ cái viết hoa
    converted_d = s.upper()
    print(f"d) Chuỗi sau khi chuyển tất cả chữ cái thành chữ hoa: {converted_d}")

    # e) Chuyển đổi tất cả các chữ cái viết hoa trong chuỗi thành chữ cái viết thường
    converted_e = s.lower()
    print(f"e) Chuỗi sau khi chuyển tất cả chữ cái thành chữ thường: {converted_e}")

    # f) Đảo ngược chuỗi đã nhập
    reversed_f = s[::-1]
    print(f"f) Chuỗi sau khi đảo ngược: {reversed_f}")

# Gọi hàm
manipulate_string()
