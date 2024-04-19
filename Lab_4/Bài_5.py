# Tiếp tục hỏi người dùng cho đến khi họ chọn không
while True:
    # Lấy đầu vào từ người dùng
    num1 = float(input("Nhập vào số thứ nhất: "))
    num2 = float(input("Nhập vào số thứ hai: "))

    # Thực hiện các phép toán
    cong = num1 + num2
    tru = num1 - num2
    nhan = num1 * num2
    chia = num1 / num2

    # Hiển thị kết quả các phép toán
    print(f"Kết quả cộng: {cong}")
    print(f"Kết quả trừ: {tru}")
    print(f"Kết quả nhân: {nhan}")
    print(f"Kết quả chia: {chia}")

    # Tính toán lũy thừa và căn bậc hai
    so_mu = float(input("Nhập số mũ: "))
    luy_thua = num1 ** so_mu
    print(f"Kết quả lũy thừa: {luy_thua}")

    can_bac_2 = float(input("Nhập số cần tính căn bậc hai: "))
    can_bac_hai = can_bac_2 ** 0.5
    print(f"Kết quả tính căn bậc hai: {can_bac_hai}")

    # Hỏi người dùng có muốn tiếp tục không
    tiep_tuc = input("Bạn có muốn tiếp tục không (yes/no)? ")
    if tiep_tuc != "yes":
        break