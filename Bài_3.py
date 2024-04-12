from collections import Counter

# Nhập chuỗi và từ cần tìm từ người dùng
s = input("Nhập một chuỗi: ")
word = input("Nhập từ cần tìm: ")

# Tìm chỉ số của từ trong chuỗi
index = s.find(word)
if index != -1:
    print(f"Từ '{word}' xuất hiện ở vị trí {index} trong chuỗi.")
else:
    print(f"Từ '{word}' không xuất hiện trong chuỗi.")

# Tìm từ xuất hiện nhiều nhất trong chuỗi
word_counts = Counter(s.split())
most_common_word, count = word_counts.most_common(1)[0]
print(f"Từ xuất hiện nhiều nhất trong chuỗi là '{most_common_word}', xuất hiện {count} lần.")
