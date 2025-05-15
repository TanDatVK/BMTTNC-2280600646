def dao_nguoc_lst(lst):
    return lst[::-1]
chuoi = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
num = list(map(int, chuoi.split(",")))
list_dao = dao_nguoc_lst(num)
print("List sau khi dao nguoc la: ", list_dao)