def find_min_max(numbers):
    min_num = float('inf')
    max_num = float('-inf')
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

numbers = []
while True:
    num = input("Nhập vào một số (hoặc nhập 'done' để kết thúc): ")
    if num.lower() == "done":
        break
    try:
        num = float(num)
        numbers.append(num)
    except ValueError:
        print("Số vừa nhập không hợp lệ. Vui lòng nhập lại.")

if not numbers:
    print("Không có số nào được nhập vào.")
else:
    min_num, max_num = find_min_max(numbers)
    print(f"Số nhỏ nhất trong dãy số là {min_num}.")
    print(f"Số lớn nhất trong dãy số là {max_num}.")