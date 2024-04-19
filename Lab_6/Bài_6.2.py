# Hàm để nhập một ma trận vuông
def nhap_ma_tran_vuong():
    n = int(input("Nhập kích thước của ma trận vuông: "))
    return [[float(input(f"Nhập phần tử tại vị trí ({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)]

# Hàm để kiểm tra ma trận đối xứng
def kiem_tra_ma_tran_doi_xung(ma_tran):
    return all(ma_tran[i][j] == ma_tran[j][i] for i in range(len(ma_tran)) for j in range(len(ma_tran[i])))

# Nhập ma trận vuông
ma_tran = nhap_ma_tran_vuong()

# Kiểm tra và thông báo nếu ma trận đã nhập là ma trận đối xứng
if kiem_tra_ma_tran_doi_xung(ma_tran):
    print("Ma trận đã nhập là ma trận đối xứng.")
else:
    print("Ma trận đã nhập không phải là ma trận đối xứng.")
