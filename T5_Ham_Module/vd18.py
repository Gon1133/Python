def In_UocSo(n,i):
    if i>0:
        if n%i==0:
            print(i)
        In_UocSo(n,i-1)
n=int(input("Nhap so nguyen duong n = "))
print("Cac uoc so cua", n, "la:")
In_UocSo(n,n)