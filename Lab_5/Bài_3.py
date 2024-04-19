text = input("Nhập văn bản: ")
word = input("Nhập từ cần tìm: ")

# Hiển thị vị trí của từ trong văn bản
print(f"Vị trí của từ '{word}' trong văn bản là: {text.find(word)}")

# Tìm từ xuất hiện nhiều nhất
most_common_word = max(set(text.split()), key=text.split().count)

# Hiển thị từ xuất hiện nhiều nhất
print(f"Từ xuất hiện nhiều nhất trong văn bản là '{most_common_word}'")
