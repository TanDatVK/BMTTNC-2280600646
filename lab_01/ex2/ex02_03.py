while True:
    try:
        num = int(input("Nhập vào một số nguyên: "))
        break  
    except ValueError:
        print("⚠️ Lỗi: Bạn phải nhập một số nguyên. Vui lòng thử lại!")
if num % 2==0:
    print ("Day la so chan")
else:
    print("Day la so le")

