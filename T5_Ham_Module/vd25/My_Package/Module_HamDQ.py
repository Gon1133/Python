def GiaiThua(n):
    if n==1:
        return 1
    else:
        return GiaiThua(n-1)*n

def UCLN(a, b):
    if a==b:
        return a
    elif a<b:
        return UCLN(a, b-a)
    else:
        return UCLN(a-b, b)


def In_UocSo(n,i):
    if i>0:
        if n%i==0:
            print(i)
        In_UocSo(n,i-1)