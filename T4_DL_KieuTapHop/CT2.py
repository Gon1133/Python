m = int(input("Nhập số lượng phần tử:"))
ds= []
for i in range(0,m):
    s = float(input("Nhập số thực:"))
    ds.append(s)
print("Danh sách sau khi nhập là:")
print(ds)
x = float(input("Nhập số thực x cần tìm:"))
if x in ds:
    vt = ds.index(x)
    print("Vị trí xuất hiện đầu tiên của",x,"là:",vt)
else:
    print("Không tồn tại",x,"trong danh sách")
y=float(input("Nhập số thực y cần xóa:"))
if y in ds:
    vt=len(ds)-1
    while ds[vt] !=y:
        vt=vt-1
    del ds[vt]
    print("Danh sách sau khi xóa",y,"sau cùng là:")
    print(ds)
else:
    print("Không tồn tại",y,"sau cùng là:")
    print(ds)
n = int(input("Nhập số lượng phần tử cần sao chép:"))
k = int(input("Nhập ví trí cần sao chép:"))
dsm = ds[k:k+n]
print("Danh sách được sao chéo là:")
print(dsm)