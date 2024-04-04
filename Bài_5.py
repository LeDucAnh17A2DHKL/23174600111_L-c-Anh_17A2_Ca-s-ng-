while True:
    # Nhập hai số từ bàn phím
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))

    # Thực hiện các phép toán
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    
    if b != 0:
        print(f"{a} / {b} = {a / b}")
        print(f"{a} % {b} = {a % b}")
    else:
        print("Không thể chia cho 0")

    # Hỏi người dùng có muốn tiếp tục không
    tieptuc = input("Bạn có muốn tiếp tục không? (y/n): ")
    
    if tieptuc.lower() != 'y':
        break
