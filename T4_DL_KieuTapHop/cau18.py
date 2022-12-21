m = int(input("Nhap hang:"))
n = int(input("Nhap cot:"))
arr = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j]=i*j
print("Ma tran vua khoi tao la:")
for i in range(m):
    print(arr[i])

k = int(input("Nhap uoc so k:"))
d = 0
for i in range(m):
    for j in range(n):
        if(arr[i][j]!=0 and k%arr[i][j]==0):
            d+=1
print("Co",d,"phan tu la uoc so cua",k)

c= int(input("Nhap cot c:"))
t  = 0
for i in range(m):
    t +=arr[i][c]
print("Tong phan tu cot",c,"la",t)

h = int(input("Nhap hang:"))
arr[h]=sorted(arr[h],reverse=True)
print("Ma tran da sap xep la:")
for i in range(0,m):
    print(arr[i])






