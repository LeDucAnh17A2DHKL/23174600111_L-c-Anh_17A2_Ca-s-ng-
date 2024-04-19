def tim_ky_tu_chung_ngan_nhat(chuoi1, chuoi2):
    # Tìm các ký tự chung và lưu vào một chuỗi mới
    ky_tu_chung = ''
    for ky_tu in chuoi1:
        if ky_tu in chuoi2 and ky_tu not in ky_tu_chung:
            ky_tu_chung += ky_tu
    return ky_tu_chung

# Sử dụng ví dụ chuỗi để kiểm tra
chuoi1 = "subsequence"
chuoi2 = "subsequent"
tim_ky_tu_chung_ngan_nhat(chuoi1, chuoi2)
