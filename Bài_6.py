def số_thành_từ (n):
    num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                  6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    num2words2 = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                  'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    num2words3 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
                  "Sixty", 'Seventy', 'Eighty', 'Ninety']

    if n > 0:
        if n < 10:
            return num2words1[n]
        elif n <= 99:
            tens, below_ten = divmod(n, 10)
            if below_ten == 0:
                return num2words3[tens - 1]
            elif 10 < n < 20:
                return num2words2[below_ten - 1]
            else:
                return f'{num2words3[tens - 1]} {num2words1[below_ten]}'
    else:
        return "The number is not positive"

try:
    n = int(input("Nhập một số: "))
    print(số_thành_từ(n))
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên dương hợp lệ.")
