def UocSo(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end="\t")

def BoiSo7():
    i=7
    while i<101:
        print(i,end=" ")
        i+=7

def LuyThua(x,n):
    kq=1
    for i in range(1,n+1):
        kq*=x
    return kq