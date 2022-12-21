def GiaiThua(n):
    if n==1:
        return 1
    else:
        return GiaiThua(n-1)*n
n=int(input("Nhap so nguyen duong n = "))
print(n,"! =",GiaiThua(n))