# Nhập ba số nguyên dương từ bàn phím
try:
    a, b, c = map(int, input("Nhập vào 3 số nguyên dương: ").split())
    
    if a <= 0 or b <= 0 or c <= 0:
        print("Vui lòng nhập vào số nguyên dương.")
    else:
        # Tìm số lớn thứ hai trong ba số
        if (a > b and a < c) or (a < b and a > c):
            print(f"Số lớn thứ hai là: {a}")
        elif (b > a and b < c) or (b < a and b > c):
            print(f"Số lớn thứ hai là: {b}")
        elif (c > a and c < b) or (c < a and c > b):
            print(f"Số lớn thứ hai là: {c}")
        else:
            print("Không có số lớn thứ hai vì có ít nhất hai số giống nhau.")

except ValueError:
    print("Vui lòng nhập vào số nguyên.")
