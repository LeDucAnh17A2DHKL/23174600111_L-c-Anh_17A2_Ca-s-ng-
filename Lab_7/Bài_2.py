# Khởi tạo một dictonary trống để lưu trữ thông tin sinh viên
sinh_vien = {}

# Nhập thông tin sinh viên từ bàn phím
for i in range(10):
    ten = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm thi của sinh viên: "))
    sinh_vien[ten] = diem

# Khởi tạo một dictonary để đếm số lượng sinh viên tại mỗi mức độ học lực
muc_do_hoc_luc = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

# Phân loại học lực và đếm số lượng sinh viên tại mỗi mức độ học lực
for ten, diem in sinh_vien.items():
    if diem < 4.0:
        muc_do_hoc_luc["F"] += 1
    elif 4.0 <= diem <= 5.4:
        muc_do_hoc_luc["D"] += 1
    elif 5.5 <= diem <= 6.9:
        muc_do_hoc_luc["C"] += 1
    elif 7.0 <= diem <= 8.4:
        muc_do_hoc_luc["B"] += 1
    elif 8.5 <= diem <= 10.0:
        muc_do_hoc_luc["A"] += 1

# In số lượng sinh viên tại mỗi mức độ học lực
print("Mức độ học lực:")
for muc_do, so_luong in muc_do_hoc_luc.items():
    print(f"{muc_do}: {so_luong} sinh viên")