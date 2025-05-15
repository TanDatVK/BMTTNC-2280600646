def truy_cap_phan_tu(tuple_data):
    first_num = tuple_data[0]
    final_num = tuple_data[-1]
    return first_num,final_num
intput_tuple = eval(input("Moi nhap cac phan tu: "))
first, final = truy_cap_phan_tu(intput_tuple)
print ("Phan tu dau tien la: " + str(first) + " va phan tu cuoi cung la: " + str(final) )