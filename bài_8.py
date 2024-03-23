def kiem_tra_duong_thang(a1, b1, c1, a2, b2, c2):
    if a1*b2 - a2*b1 == 0:
        if a1*c2 - a2*c1 == 0 and b1*c2 - b2*c1 == 0:
            return "Đường thẳng trùng nhau"
        else:
            return "Đường thẳng song song"
    elif (a1*a2 + b1*b2) / ((a1**2 + b1**2)**0.5 * (a2**2 + b2**2)**0.5) == 0:
        return "Đường thẳng vuông góc"
    else:
        return "Đường thẳng cắt nhau"

# Nhập hệ số của hai đường thẳng
# ax + by + c = 0
a1 = float(input("Nhập hệ số a của đường thẳng thứ nhất: "))
b1 = float(input("Nhập hệ số b của đường thẳng thứ nhất: "))
c1 = float(input("Nhập hệ số c của đường thẳng thứ nhất: "))
a2 = float(input("Nhập hệ số a của đường thẳng thứ hai: "))
b2 = float(input("Nhập hệ số b của đường thẳng thứ hai: "))
c2 = float(input("Nhập hệ số c của đường thẳng thu hai: "))

# Kiểm tra mối quan hệ giữa hai dườn thẳng
print(kiem_tra_duong_thang(a1, b1, c1, a2, b2, c2))
