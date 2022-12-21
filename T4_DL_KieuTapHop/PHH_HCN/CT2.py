m=int(input("nhap so luong ptu: "))
ds=[]
for i in range(m):
    s=float(input("nhap so thuc: "))
    ds.append(s)
print("danh sach sau khi nhap la: ")
print(ds)
x=float(input("nhap so thuc x can tim: "))
if x in ds:
    vt = ds.index(x)
    print("Vi tri xuat hien dau tien cua",x,"la",vt)
else:
    print("Khong ton tai",x,"trong danh sach")
y=float(input("nhap so thuc y can xoa:"))
if y in ds:
    vt = len(ds)-1
    while ds[vt]!=y:
        vt=vt-1
    del ds[vt]
    print("danh sach sau khi xoa", y,"sau cung la")
    print(ds)
else:
    print("khong ton tai",y,"trong danh sach")
n=int(input("nhap so luong ptu can sao chep:"))
k=int(input("nhap vi tri can sao chep:"))
dsm=ds[k:k+n]
print("danh sach duoc sao chep la:")
print(dsm)