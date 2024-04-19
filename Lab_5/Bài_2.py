
def chuoi_con_chung_ngan_nhat(chuoi1, chuoi2):
    # Khởi tạo chuỗi con chung ngắn nhất là None
    chuoi_con_chung_ngan_nhat = None

    # Duyệt qua tất cả các chuỗi con của chuoi1
    for i in range(len(chuoi1)):
        for j in range(i + 1, len(chuoi1) + 1):
            # Lấy chuỗi con hiện tại
            chuoi_con = chuoi1[i:j]

            # Kiểm tra xem chuỗi con có trong chuoi2 không
            if chuoi_con in chuoi2:
                # Nếu đây là chuỗi con chung đầu tiên hoặc nó ngắn hơn chuỗi ngắn nhất hiện tại
                if chuoi_con_chung_ngan_nhat is None or len(chuoi_con) < len(chuoi_con_chung_ngan_nhat):
                    # Cập nhật chuỗi con chung ngắn nhất
                    chuoi_con_chung_ngan_nhat = chuoi_con

    # Trả về chuỗi con chung ngắn nhất
    return chuoi_con_chung_ngan_nhat

# Thử nghiệm chương trình
chuoi1 = "X"
chuoi2 = "thế giới, in chào!"
print(chuoi_con_chung_ngan_nhat(chuoi1, chuoi2))
