def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan, tach boi dau phay")
list_so_nhi_phan = chuoi_so_nhi_phan.split(",")
so_chia_het_cho_5 = [so for so in list_so_nhi_phan if chia_het_cho_5(so)]
if len (so_chia_het_cho_5):
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la:", ket_qua)
else:
    print("Khong co gia tri nhi phan nao chia het cho 5 trong chuoi da cho")