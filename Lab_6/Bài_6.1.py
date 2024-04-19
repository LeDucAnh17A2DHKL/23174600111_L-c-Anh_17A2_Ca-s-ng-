# Hàm để nhập một ma trận
def nhap_ma_tran():
    m = int(input("Nhập số hàng: "))
    n = int(input("Nhập số cột: "))
    return [[float(input(f"Nhập phần tử tại vị trí ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]

# Hàm để tính tổng của tất cả các phần tử trong một ma trận
def tong_ma_tran(ma_tran):
    return sum(sum(hang) for hang in ma_tran)

# Hàm để tính tích của hai ma trận
def tich_hai_ma_tran(ma_tran1, ma_tran2):
    return [[sum(a*b for a, b in zip(hang_ma_tran1, cot_ma_tran2)) for cot_ma_tran2 in zip(*ma_tran2)] for hang_ma_tran1 in ma_tran1]

# Hàm để tính chuyển vị của một ma trận
def chuyen_vi_ma_tran(ma_tran):
    return list(map(list, zip(*ma_tran)))

# Nhập ma trận đầu tiên
ma_tran1 = nhap_ma_tran()

# Tính và in tổng của tất cả các phần tử trong ma trận đầu tiên
print(f"Tổng của tất cả các phần tử trong ma trận đầu tiên là {tong_ma_tran(ma_tran1)}.")

# Nhập ma trận thứ hai
ma_tran2 = nhap_ma_tran()

# Nếu số cột trong ma trận đầu tiên bằng số hàng trong ma trận thứ hai, tính và in tích của hai ma trận
if len(ma_tran1[0]) == len(ma_tran2):
    print(f"Tích của hai ma trận là:\\n{tich_hai_ma_tran(ma_tran1, ma_tran2)}")
else:
    print("Tích của hai ma trận không xác định.")

# Tính và in chuyển vị của ma trận đầu tiên
print(f"Chuyển vị của ma trận đầu tiên là:\\n{chuyen_vi_ma_tran(ma_tran1)}")
