n=int(input("nhập số cột của ma trận: "))
m=int(input("nhập số hàng của ma trận: "))
arr=[]
for i in range(m):
    arrcon=[]
    for j in range(n):
        print("[%d][%d] = "%(i,j), end="")
        t = int(input())
        arrcon.append(t)
    arr.append(arrcon)
print("Ma tran vua nhap la: ")
for i in range(0,m):
    for j in range(0,n):
        print(arr[i][j],end=" ")
    print()

#đếm số ptu là ước số của k
k = int(input("nhap k: "))
d=0
for i in range(m):
    for j in range(n):
        if arr[i][j]!=0:
            if k%arr[i][j]==0:
                d+=1
print("co %d ptu la uoc so cua %d"%(d,k))

#tính tổng các ptu nằm trên cột c
c=int(input("nhap cot muon tinh tong: "))
while c<0 or c>=n:
    c = int(input("nhap cot muon tinh tong: "))
s=0
for i in range(m):
    s += arr[i][c]
print("tong cac ptu nam tren cot %d = %d"%(c,s))

#sắp xếp giảm dần các ptu nằm trên hàng h
h=int(input("nhap hang muon sap xep: "))
while h<0 or h>=m:
    h = int(input("nhap hang muon sap xep: "))
for i in range(n-1):
    for j in range(i+1,n):
        if arr[h][i] < arr[h][j]:
            t = arr[h][i]
            arr[h][i] = arr[h][j]
            arr[h][j] = t
#sap xep bang ham sorted
arr[h] = sorted(arr[h],reverse=True)

print("ma tran vua sap xep giam dan hang %d la: "%h)
for i in range(m):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
