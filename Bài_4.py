# Định nghĩa hàm để tính tổng
def calculate_sums(n):
    # Kiểm tra nếu n lớn hơn 10
    if n <= 10:
        return "Vui lòng nhập số nguyên lớn hơn 10."

    # a)
    s1 = 0
    i = 1
    while i <= n and s1 + 6**i <= n:
        s1 += 6**i
        i += 1

    # b)
    s2 = 0
    i = 3
    while i <= n and s2 + (1 / i) <= n:
        s2 += (1 / i)
        i += 2

    # c)
    s3 = -12 
    a = -12 
    d = -10 
    while abs(a) < abs(n):
        a += d 
        if abs(s3 + a) < abs(n):
            s3 += a 

    # d)
    s4, a, dA=0,0,0.5 # S4 là tổng của chuỗi; 'a' là số hạng hiện tại; 'dA' là sự khác biệt chung giữa các số hạng.
    while True: # Vòng lặp vô hạn để tiếp tục thêm số hạng cho đến khi tổng của chúng vượt quá 'n'.
        if s4+a+dA<=abs(n): # Nếu thêm một số hạng khác không vượt quá 'n'...
            a+=dA # ...tăng số hạng hiện tại lên theo sự khác biệt chung...
            s4+=a # ...và thêm nó vào tổng.
        else: break # Nếu thêm một số hạng KHÁC sẽ vượt quá 'n', thoát khỏi vòng lặp.

    return s1, s2, s3, s4

# Kiểm tra hàm 
n = 69
s1, s2, s3, s4 = calculate_sums(n)
print(f"Với n = {n}, các tổng là:\nS1: {s1}\nS2: {s2}\nS3: {s3}\nS4: {s4}")
