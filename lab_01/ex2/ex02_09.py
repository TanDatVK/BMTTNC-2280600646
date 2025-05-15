def kiem_tra_snt(n):
    if n <=1:
        return False
    for i in range (2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Moi ban nhap so can kiem tra: "))
if kiem_tra_snt(number):
    print("Day la so nguyen to:", number)
else:
    print("Day hong phai la so nguyen to")