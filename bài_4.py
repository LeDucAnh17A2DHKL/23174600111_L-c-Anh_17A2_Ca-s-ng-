# Nhập điểm số từ người dùng
diem = float(input("Nhập điểm số của bạn: "))

# Kiểm tra và in ra thông báo tương ứng
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ. Vui lòng nhập lại.")
elif diem < 5:
    print("Điểm kém")
elif diem < 7:
    print("Điểm trung bình")
elif diem < 8.5:
    print("Điểm khá")
else:
    print("Điểm tốt")
