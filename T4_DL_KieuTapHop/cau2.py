n = int(input("Nhập số lượng phần tử:"))
ds=[]
for i in range(0,n):
    m =float(input("Nhập pt số thực:"))
    ds.append(m)
print("Danh sách vừa nhập:", ds)
k = int(input("Nhập vị trí muốn xóa:"))
ds.pop(k)
n=n-1
print("Danh sách sau khi xóa: ",ds)
ds1=[]
ds2=[]
for i in ds:
    if (i-int(i))<0.5:
        ds2.append(i)
    else:
        ds1.append(i)
print("Danh sách 1:",ds1)
print("Danh sách 2:",ds2)
ds1.sort(reverse=False)
ds2.sort(reverse=True)
print("Danh sách 1 sau sắp xếp:",ds1)
print("Danh sách 2 sau sắp xếp:",ds2)

ds=[]
if len(ds1) > len(ds2):
    for i in range(0,len(ds2)):
        ds.append(ds1[i])
        ds.append(ds2[i])
    for j in range(i+1,len(ds1)):
        ds.append(ds1[j])
else:
    for i in range(0,len(ds1)):
        ds.append(ds1[i])
        ds.append(ds2[i])
    for j in range(i+1,len(ds2)):
        ds.append(ds2[j])



print("danh sao khi tron:")
for i in ds:
    print(i,end=" ")
