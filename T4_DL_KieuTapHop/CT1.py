n=int(input("Nhập số lượng phần tử:"))
ds = []
for i in range(0,n):
    s= int(input("Nhập số nguyên:"))
    ds.append(s)
print("Danh sách sau khi nhập là: ")
for i in ds:
    print(i,end='\t')
print("\nGía trị của phần tử lớn nhất là:",max(ds))
print("Giá trị của phần tử nhỏ nhất:",min(ds))
k = int(input("Nhập giá trị để thêm:"))
vtg = int(len(ds)/2)
ds.insert(vtg, k)
ds.insert(0,k)
ds.insert(len(ds),k)
print("Danh sách sau khi thêm là: ",ds)