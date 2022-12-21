import math
n=int(input("nhap so luong ptu: "))
list=[]
for i in range(n):
    t=input("nhap so thap phan 6 chu so:")
    list.append(t)
print(list)
#tao tup co ptu %5
ds=[]
for i in list:
    dec = 0
    for j in range(len(i)):
        if i[j]=="1":
            dec = dec + 2**(5-j)
    if dec%5==0:
        ds.append(i)
tup=tuple(ds)
print("tuple moi:",tuple(tup))
#them ptu %5 and <30
# for i in ds:
#     dec=0
#     for j in range(len(i)):
#         if i[j]=="1":
#             dec = dec + 2**(5-j)
#             if dec



