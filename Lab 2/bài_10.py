# Hàm để kiểm tra xem có suất chiếu không dựa trên loại phim và thời gian
def kiem_tra_suatchieu(loai_phim, thoi_gian):
    # Định nghĩa các ràng buộc cho từng loại phim
    rang_buoc = {
        'Hành động': ['sáng', 'trưa', 'chiều', 'tối'],
        'Kinh dị': ['tối'],
        'Tình cảm': ['tối'],
        'Hài hước': ['sáng', 'trưa', 'chiều', 'tối'],
        'Hoạt hình': ['sáng', 'trưa']
    }
    
    # Kiểm tra xem loại phim và thời gian có khớp với ràng buộc không
    if loai_phim in rang_buoc and thoi_gian in rang_buoc[loai_phim]:
        return f"Có suất chiếu {loai_phim} vào {thoi_gian}."
    else:
        return "Không có suất chiếu."

# Nhập thông tin từ người dùng
loai_phim = input("Nhập loại phim bạn muốn xem (Hành động, Kinh dị, Tình cảm, Hài hước, Hoạt hình): ")
thoi_gian = input("Nhập thời gian bạn muốn xem (sáng, trưa, chiều, tối): ")

# In kết quả ra màn hình
print(kiem_tra_suatchieu(loai_phim.strip(), thoi_gian.strip()))
