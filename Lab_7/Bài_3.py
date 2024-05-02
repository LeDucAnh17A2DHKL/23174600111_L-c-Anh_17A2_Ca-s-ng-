import collections

# Văn bản đã được cung cấp
text = "Last Sunday was very hot. Temperature was above 40 degree even in the morning. One could not dare to go outside. As if it was not enough, electricity went off due to fault in transformer. Without fan and cooler it was really unbearable. We used hand fans, drank lots of cold beverages, but all seems ineffective before hot and dry weather. That day appeared too long to pass. In the evening some clouds gathered in the sky. A light shower brought the mercury down. We took breath of relief."

# Chuyển đổi sang chữ thường và loại bỏ dấu
text = ''.join(e for e in text if (e.isalnum() or e.isspace())).lower()

# Chia văn bản thành các từ
words = text.split()

# Đếm số lần xuất hiện của từng từ
word_counts = collections.Counter(words)

# Tìm từ xuất hiện nhiều nhất và ít nhất
most_common_word = word_counts.most_common(1)[0][0]
least_common_word = word_counts.most_common()[:-2:-1][0][0]

print(f"Từ xuất hiện nhiều nhất: {most_common_word}")
print(f"Từ xuất hiện ít nhất: {least_common_word}")