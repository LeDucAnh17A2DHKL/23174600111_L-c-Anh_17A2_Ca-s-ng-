while True:
    try:
        number = int(input("Nhập một số nguyên: "))
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

number_of_digits = len(str(number))
print(f"Số chữ số của số nguyên {number} là {number_of_digits}.")