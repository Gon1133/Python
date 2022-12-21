def LuyThua(x,n):
    kq=1
    for i in range(1,n+1):
        kq*=x
    return kq
a = LuyThua(5,3)
b = LuyThua(3,5)
print(a)
print(b)
y = LuyThua(x=5,n=3)
z = LuyThua(n=3,x=5)
