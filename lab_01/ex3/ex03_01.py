def tinh_tong_chan_list(lst):
    tong = 0
    for i in lst:
        if i % 2 == 0:
            tong += i
    return tong

mang_str = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
num = list(map(int, mang_str.split(",")))

tong_chan = tinh_tong_chan_list(num)
print("Tổng các số chẵn trong mảng là:", tong_chan)
