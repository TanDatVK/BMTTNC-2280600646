def diem_so_lan_show(lst):
    dem = {}
    for item in lst:
        if item in dem:
            dem[item]+= 1
        else:
            dem[item] = 1
    return dem
input_string = input ("Nhap danh sach cac tu cach nhau bang dau cach: ")
word_list = input_string.split()
so_lan_show = diem_so_lan_show(word_list)
print("So lan xuast hien cua cac phan tu: " , so_lan_show)