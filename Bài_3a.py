# Duyệt qua các số trong khoảng từ 100 đến 1000
for num in range(100, 1001):
    if num > 1: # số nguyên tố lớn hơn 1
        for i in range(2, num):
            if (num % i) == 0: # không phải là số nguyên tố
                break
        else:
            print(num)
