def tao_tupple(lst):
    return tuple(lst)

input_list = input("Mời nhập danh sách các số vào bàn phím, cách bằng dấu phẩy: ")
num = list(map(int, input_list.split(",")))  
my_tuple = tao_tupple(num)
print("List:", num)
print("Tuple từ list:", my_tuple)
print("Kiểu dữ liệu của tuple:", type(my_tuple)) 