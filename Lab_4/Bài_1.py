tổng_số_đã_nhập = 0
số_chẵn = []
số_lẻ = []

while tổng_số_đã_nhập <= 1000:
    số = int(input("Nhập vào một số nguyên dương: "))
    tổng_số_đã_nhập += số

    if số % 2 == 0:
        số_chẵn.append(số)
    else:
        số_lẻ.append(số)

print("\nCác số lẻ đã nhập là:")
for số_lẻ_nhập in số_lẻ:
    print(số_lẻ_nhập)

print("\nCác số chẵn đã nhập là:")
for số_chẵn_nhập in số_chẵn:
    print(số_chẵn_nhập)

print("Tổng số lượng số nguyên đã nhập là: ", len(số_lẻ) + len(số_chẵn))