# Nhập một số nguyên từ người dùng
user_input = int(input("Nhập vào một số nguyên: "))

# Trích xuất chữ số hàng nghìn hoặc in 0 nếu không tồn tại
try:
    # Chuyển đổi thành chuỗi để dễ dàng trích xuất chữ số bằng cách sử dụng chỉ mục
    str_input = str(user_input)
    
    # In chữ số hàng nghìn nếu tồn tại
    print(str_input[-4])
except IndexError:
    # In 0 nếu không có chữ số hàng nghìn
    print(0)
