# Nhập hệ số a và b
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Kiểm tra nếu cả hai hệ số đều bằng không
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm.")
# Kiểm tra nếu hệ số a bằng không
elif a == 0:
    print("Phương trình vô nghiệm.")
else:
    # Tính nghiệm của phương trình bậc nhất ax + b = 0
    x = -b / a
    print(f"Nghiệm của phương trình là x = {x}")
