def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(s):
    return ''.join(c for c in s if c in '2357')

def check_string(s):
    filtered = filter_primes(s)
    if filtered and is_prime(int(filtered)):
        print(f"Chuỗi sau khi loại bỏ các ký tự không phải số nguyên tố: {filtered}")
        print("Chuỗi kết quả là một số nguyên tố.")
    else:
        print(f"Chuỗi sau khi loại bỏ các ký tự không phải số nguyên tố: {filtered}")
        print("Chuỗi kết quả không phải là một số nguyên tố.")

# Kiểm tra hàm với chuỗi mẫu
s = "Hello, how are you? 2357"
check_string(s)
