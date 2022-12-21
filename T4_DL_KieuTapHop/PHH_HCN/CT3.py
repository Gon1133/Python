n=int(input("nhap so luong ptu"))
ds=[]
for i in range(n):
    s=input("nhap chuoi ky tu:")
    ds.append(s)
print("danh sach sau khi nhap la:")
print(ds)
dsn=ds.copy()
dsn.reverse()
print("danh sach dao nguoc cua danh sach hien co la:")
print(dsn)
i=0
kt=True
while i<len(ds) and kt==True:
    if(ds[i]==dsn[i]):
        i=i+1
    else:
        kt=False
if kt==True:
    print("danh sach doi xung")
else:
    print("danh sach ko doi xung")
st=input("nhap chuoi ku tu:")
while st in ds:
    ds.remove(st)
print("danh sach sau khi xoa chuoi",st,":")
print(ds)
ds.sort(reverse=True)
print("danh sach sau khi sap xep la:")
print(ds)