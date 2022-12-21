import math
arr=[]
while True:
    t = int(input("nhap so nguyen: "))
    if (t!=0):
        arr.append(t)
    else: break
print("Danh sach da nhap:",arr)



def KtraNgTo(n):
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            return False
        i+=1
    return True

def InListNgTo(arr):
    ListNguyenTo=[]
    for i in range(0,len(arr)):
        if KtraNgTo(arr[i]):
            ListNguyenTo.append(arr[i])
    return ListNguyenTo


ListDuong=[x for x in arr if x>0]

print("List cac so Duong:",ListDuong)

ListChan=filter(lambda x: x%2==0, arr)

print("List cac so chan:",ListChan)

ListCP=[x for x in arr if pow(x,0.5)==int(pow(x,0.5))]

print("List cac so chinh phuong:",ListCP)

print("List cac so nguyen to:",InListNgTo(arr))



