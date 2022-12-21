from operator import itemgetter
ds = []
print('Nhap chuoi da dong:')
while True:
    s = input()
    if not s:
        break
    ds.append(tuple(s.split(',')))
print("Cac dong duoc chuyen thanh cac tuple la:")
for i in ds:
    print(i)
ds = sorted(ds, key=itemgetter(0,1,2))
print('Cac tuple sau khi sap xep la:')
for i in ds:
    print(i)
