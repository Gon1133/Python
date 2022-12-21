# a. nhap list gom n ptu so nguyen
def NhapListNguyen(arr,n):
    for i in range(0,n):
        t=int(input("nhap so nguyen: "))
        arr.append(t)
    return arr

# b. in list gom n ptu so nguyen
def InListNguyen(arr):
    print(arr)

# c. tra ve list cac ptu trùng bị xóa
def ListKoTrung(arr):
    a = list(set(arr))
    return a

# d.tra ve list moi bang cach tron xen ke 2 list da co
def TronList(arr1,arr2):
    arr=[]
    if (len(arr1) > len(arr2)):
        for i in range(0,len(arr2)):
            arr.append(arr1[i])
            arr.append(arr2[i])
        for j in range(i+1,len(arr1)):
            arr.append(arr1[j])
    else:
        for i in range(0,len(arr1)):
            arr.append(arr1[i])
            arr.append(arr2[i])
        for j in range(i+1,len(arr2)):
            arr.append(arr2[j])
    return arr

def Giao2List(arr1,arr2):
    arr=[]
    for i in arr1:
        if i in arr2:
            arr.append(i)
    return arr
    
        

arr=[]
n = int(input("nhap so luong: "))
NhapListNguyen(arr,n)
print("List da nhap: ")
InListNguyen(arr)
print("List da xoa cac ptu trung:",ListKoTrung(arr))
print("List dc tron xen ke tu 2 list da co:", TronList(arr,ListKoTrung(arr)))
print("List gom cac ptu giao voi nhau:",Giao2List(arr,ListKoTrung(arr)))