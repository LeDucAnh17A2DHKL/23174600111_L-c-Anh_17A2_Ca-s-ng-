# Input: A positive integer
n = int(input("Nhập vào một số nguyên dương: "))

# Ensure the input is positive
if n < 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    count = 0
    
    # Using while loop to count the number of digits
    while n > 0:
        count += 1
        n //= 10
    
    print("Số chữ số của số nguyên đó là:", count)
