try:
    x = input("nhap bieu thuc toan hoc: ")
    print("ket qua bieu thuc toan hoc la:",eval(x))
except SyntaxError:
    print("thieu doi so cua phep toan")
except ValueError:
    print("Gia tri khong hop le")
except ZeroDivisionError:
    print("khong chia duoc cho 0")