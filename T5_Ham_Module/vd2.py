def UocSo(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end="\t")
m = int(input("Nhập số nguyên dương m = "))
print("Các ước số của",m,"là:")
UocSo(m)
