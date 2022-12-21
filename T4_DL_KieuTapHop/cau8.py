n = int(input("Nhap so luong phan tu:"))
ds=[]
for i in range(0, n):
    s = input("Nhap chuoi so nhi phan 6 so:")
    ds.append(s)
print("Danh sach sau khi nhap:",ds)
chiahet5 = ()
for i in ds:
    if int(i,2)%5==0:
        chiahet5 +=(i,)
print('Tupple chua cac so chia het cho 5 la:',chiahet5)
i = 5
while i<30:
    st = bin(i) #radang: 0bxxxx
    tam = st[2:].zfill(6)
    if tam not in chiahet5:
        chiahet5 += (tam,)
    i += 5
print("Tupple sau khi them la:",chiahet5)