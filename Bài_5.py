def merge_strings(s1, s2):
    # Tạo một danh sách để lưu kết quả
    result = []
    # Lấy độ dài lớn nhất của hai chuỗi
    max_length = max(len(s1), len(s2))
    for i in range(max_length):
        # Thêm ký tự từ chuỗi s1 nếu có
        if i < len(s1):
            result.append(s1[i])
        # Thêm ký tự từ chuỗi s2 nếu có
        if i < len(s2):
            result.append(s2[i])
        # Thêm dấu gạch ngang nếu không phải là ký tự cuối cùng
        if i < max_length - 1:
            result.append('-')
    # Chuyển danh sách thành chuỗi và trả về
    return ''.join(result)

# Kiểm tra hàm với hai chuỗi mẫu
s1 = "Hello"
s2 = "World"
print(merge_strings(s1, s2))
