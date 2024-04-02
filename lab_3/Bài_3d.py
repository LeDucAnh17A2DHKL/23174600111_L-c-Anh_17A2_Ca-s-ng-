def get_divisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return divisors

def is_perfect_number(n):
    return sum(get_divisors(n)) == n

perfect_numbers = [i for i in range(2, 500) if is_perfect_number(i)]

print("Các số hoàn hảo nhỏ hơn 500:", perfect_numbers)
