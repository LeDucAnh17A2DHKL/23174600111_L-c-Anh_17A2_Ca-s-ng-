import math

# Nhập các thông số của đường thẳng ax + by + c = 0
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Nhập các thông số của đường tròn (h, k) là tâm và r là bán kính
h = float(input("Nhập h (tọa độ x của tâm): "))
k = float(input("Nhập k (tọa độ y của tâm): "))
r = float(input("Nhập r (bán kính): "))

# Tính khoảng cách từ tâm của đường tròn đến đường thẳng
distance = abs(a*h + b*k + c) / math.sqrt(a**2 + b**2)

if distance < r:
    print("Đường thẳng cắt qua đường tròn.")
elif distance == r:
    print("Đường thẳng tiếp xúc với đường tròn.")
else:
    print("Đường thẳng nằm ngoài phạm vi của đường tròn.")
