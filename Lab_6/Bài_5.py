def is_arithmetic_progression(numbers):
    if len(numbers) < 3:
        return False
    diff = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i-1] != diff:
            return False
    return True

numbers = []
while True:
    num = input("Nhập vào một số nguyên (hoặc nhập 'done' để kết thúc): ")
    if num == "done":
        break
    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        print("Số vừa nhập không hợp lệ. Vui lòng nhập lại.")

if is_arithmetic_progression(numbers):
    print("Dãy số này tạo thành cấp số cộng.")
    print("Dãy số:", numbers)
else:
    print("Dãy số không tạo thành cấp số cộng.")