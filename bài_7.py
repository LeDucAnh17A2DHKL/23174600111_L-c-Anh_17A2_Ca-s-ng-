# Nhập chiều cao và cân nặng từ người dùng
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
can_nang = float(input("Nhập cân nặng của bạn (kg): "))

# Tính BMI
bmi = can_nang / (chieu_cao ** 2)

# Phân loại BMI
if bmi < 18.5:
    phan_loai = "Gầy"
elif bmi < 24.9:
    phan_loai = "Bình thường"
elif bmi < 29.9:
    phan_loai = "Hơi béo"
else:
    phan_loai = "Béo"

# In kết quả
print(f"Chỉ số BMI của bạn là {bmi:.2f} và bạn được phân loại là '{phan_loai}'.")

