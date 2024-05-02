kho = {"banana": 6, "apple": 5, "orange": 32, "pear": 15}
gia_tien = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# giả sử số lượng mỗi mặt hàng mua được nhập vào là 1
hoa_don = {}
for mat_hang, so_luong in kho.items():
    hoa_don[mat_hang] = {"So luong": so_luong, "Don gia": gia_tien[mat_hang], "Thanh tien": so_luong * gia_tien[mat_hang]}

print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(f"Mặt hàng: {mat_hang}")
    print(f"Số lượng: {thong_tin['So luong']}")
    print(f"Đơn giá: {thong_tin['Don gia']}")
    print(f"Thành tiền: {thong_tin['Thanh tien']}")
    print("---")