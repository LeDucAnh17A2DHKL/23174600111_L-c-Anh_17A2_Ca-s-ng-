import random
from collections import Counter

# Xác suất xuất hiện của mặt ngửa và mặt sấp
prob_heads = 0.7
prob_tails = 0.3

# Khởi tạo các cấu trúc dữ liệu
results = []  # List lưu kết quả của mỗi lần lật xu
unique_results = set()  # Set lưu các kết quả đã xuất hiện
result_prob = {}  # Dictionary lưu xác suất xuất hiện của mỗi kết quả

# Hàm lật xu với xác suất tùy chỉnh
def flip_coin():
    return random.choices(['Heads', 'Tails'], weights=[prob_heads, prob_tails])[0]

# Lặp lại quá trình lật xu 1000 lần
for _ in range(1000):
    result = flip_coin()
    results.append(result)
    unique_results.add(result)

# Tính xác suất xuất hiện của mỗi kết quả
result_count = Counter(results)
total_flips = len(results)
for result, count in result_count.items():
    result_prob[result] = count / total_flips

# Hiển thị lịch sử lật xu
print("Lịch sử lật xu:")
for result in unique_results:
    print(f"{result}: {results.count(result)} lần")

# In xác suất xuất hiện của mỗi kết quả
print("\nXác suất xuất hiện của mỗi kết quả:")
for result, probability in result_prob.items():
    print(f"{result}: {probability:.4f}")

# Lưu kết quả vào file CSV
with open("coin_flip_results.csv", "w") as file:
    file.write("Kết quả,Số lần xuất hiện,Xác suất xuất hiện\n")
    for result, probability in result_prob.items():
        count = results.count(result)
        file.write(f"{result},{count},{probability:.4f}\n")

print("\nKết quả đã được lưu vào file 'coin_flip_results.csv'")