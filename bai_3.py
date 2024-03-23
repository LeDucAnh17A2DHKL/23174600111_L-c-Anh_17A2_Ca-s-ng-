def number_to_words(num: int) -> str:
    under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens = ['', '',  # placeholders for zero and one
            "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",
            "Ninety"]
    above_1000 = {100: "Hundred", 10**3: "Thousand"}

    if num < 20:
        return under_20[num]
    
    if num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else '-' + under_20[num % 10])
    
    max_key = max([key for key in above_1000.keys() if key <= num])
    
    return number_to_words(num // max_key) + f" {above_1000[max_key]}" + ('' if num % max_key == 0 else f" {number_to_words(num % max_key)}")

try:
    user_input = int(input("Nhập một số nguyên: "))
    print(f"Số {user_input} được đọc là '{number_to_words(user_input)}'.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
