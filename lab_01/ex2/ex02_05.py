gio_lam = int (input("Nhap so gio lam moi tuan"))
luong = int(input("Nhap thu lao theo tieu chuan tren moi gio"))
gio_tieu_chuan = 44
gio_vuot_chuan= max(0, gio_lam - gio_tieu_chuan)
tong_luong = (gio_tieu_chuan  + gio_vuot_chuan * 1.5)* luong
print(f"So tien thuc linh cua nhan vien: {tong_luong}")
