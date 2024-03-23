# Nhập số lượng người từ bàn phím
so_luong_nguoi = int(input("Nhập số lượng người: "))

# Giá vé cho một người là 120000 đồng
gia_ve = 120000

# Tính tổng số tiền trước khi áp dụng giảm giá
tong_tien = so_luong_nguoi * gia_ve

# Áp dụng các loại giảm giá tùy thuộc vào số lượng người
if 2 <= so_luong_nguoi <= 4:
    tong_tien -= tong_tien * 0.05   # Giảm 5% tổng số tiền nếu có từ 2 đến 4 người
elif 5 <= so_luong_nguoi <=10:
    tong_tien -= tong_tien *0.1     # Giảm 10% tổng số tiền nếu có từ 5 đến10 người 
elif so_luong_nguoi >10:
    tong_tien -= tong_tien *0.2     # Giảm20% tổng số tiền nếu có hơn10 người 

print(f"Tổng số tiền phải trả là: {tong_tien} đồng")
