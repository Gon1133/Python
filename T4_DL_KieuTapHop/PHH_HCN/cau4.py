n=int(input("nhap so luong ptu: "))
ds=[]
for i in range(n):
    t=float(input("nhap so thuc: "))
    ds.append(t)
print("danh sch sau khi nhap la:")
for i in ds:
    print(i,end=" ")

#xoa ptu o vi tri k
k=int(input("\nnhap vi tri muon xoa: "))
ds.pop(k)
n=n-1
print("danh sach sau khi xoa la:")
for i in ds:
    print(i,end=" ")
#tach 2 list
ds1=[]
ds2=[]
for i in ds:
    if i-int(i) < 0.5:
        ds2.append(i)
        #ds.pop(i)
    else:
        ds1.append(i)
print("\ndanh sach 1: ")
for i in ds1:
    print(i," ")
print("danh sach 2: ")
for i in ds2:
    print(i," ")
ds.clear()
#sap xep
print(ds1.sort())
print(ds2.sort(reverse=True))
#tron list
if len(ds1) > len(ds2): t=len(ds1)
else: t=len(ds2)
for i in range(t):
    ds.append(ds1[i])
    ds.append(ds2[i])
print("danh sao khi tron:")
for i in ds:
    print(i,end=" ")
