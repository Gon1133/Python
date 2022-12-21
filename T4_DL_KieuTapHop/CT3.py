n = int(input("Nhập số lượng phần tử:"))
ds = []
for i in range(0, n):
     s = input("Nhập chuỗi ký tự:")
     ds.append(s)
print("Danh sách sau khi nhập là:")
print(ds)
dsn = ds.copy()
dsn.reverse()
print("Danh sách đảo ngược của danh sách hiện có là:")
print(dsn)
i = 0
kt = True
while i < len(ds) and kt == True:
     if(ds[i] == dsn[i]):
         i = i + 1
     else:
        kt = False
if kt == True:
    print("Danh sách đối xứng")
else:
     print("Danh sách không đối xứng")
st = input("Nhập chuỗi ký tự:")
while st in ds:
    ds.remove(st)
print("Danh sách sau khi xóa chuỗi", st, ":")
print(ds)
ds.sort(reverse=True)
print("Danh sách sau khi sắp xếp là:")
print(ds)
