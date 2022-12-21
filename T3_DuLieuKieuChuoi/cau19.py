st=input("Nhap chuoi:")
d1=0
a = []
for i in range(10):
    a.append(0)

for i in st:
    if i.isalpha()==False: d1+=1
    st=st.upper()
    if i.isdigit():
        a[int(i)] = a[int(i)] + 1
max = a[0]
for i in range(10):
    if max < a[i]:
        max = a[i]

print(st)
print(i,"la so xuat hien nhat, xuat hien",max,"lan")


