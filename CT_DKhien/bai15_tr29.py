n=int(input("nhap so nguyen: "))
t=0
for i in range(1,n+1):
    t = t + (i/(i+1))
print("tong can tim:",t)