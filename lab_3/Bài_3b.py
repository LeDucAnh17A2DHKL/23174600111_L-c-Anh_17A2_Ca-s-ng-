# Hàm để kiểm tra xem một số có phải là số chính phương hay không
def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = int(n**0.5)
    return sqrt*sqrt == n

# In ra tất cả các số chính phương từ 1 đến 1000
perfect_squares = [i for i in range(1, 1001) if is_perfect_square(i)]
print(perfect_squares)
