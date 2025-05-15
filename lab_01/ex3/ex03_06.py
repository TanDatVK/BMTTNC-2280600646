def xoa_phan_tu (dicionary,key):
    if key in dicionary:
        del dicionary[key]
        return True
    else:
        return False
my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
key_to_delete = 'b'
ket_qua = xoa_phan_tu(my_dict, key_to_delete)
if ket_qua:
    print("Phan tu da duoc xoa tu DIctionary: ", my_dict)
else:
    print("Khong tim thay phan tu can xoa trong Dictionary")