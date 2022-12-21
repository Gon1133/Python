n=int(input("Nhap so luong ptu: "))
ds=[]
for i in range(n):
    s=int(input("Nhap so nguyen: "))
    ds.append(s)
print("Danh sach sau khi nhap la:")
for i in ds:
    print(i, end='\t')
print("\nGia tri cua ptu lon nhat la:",max(ds))
print("Gia tri cua ptu nho nhat la",min(ds))
k=int(input("nhap gia tri de dem:"))
print("trong ds co",ds.count(k),"pt co gia tri la",k)
k=int(input("nhap gia tri de them:"))
vtg = int(len(ds)/2)
ds.insert(vtg,k)
ds.insert(0,k)
ds.insert(len(ds),k)
print(len(ds),k)
print("ds sau khi them la:",ds)