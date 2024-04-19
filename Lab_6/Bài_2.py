def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

n = int(input("Nhập vào số phần tử trong mảng: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

print("Các số nguyên tố trong mảng là:")
for i in arr:
    if is_prime(i):
        print(i)

print("Các số hoàn hảo trong mảng là:")
for i in arr:
    if is_perfect(i):
        print(i)