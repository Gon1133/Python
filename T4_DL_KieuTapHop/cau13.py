st = input("nhap chuoi gom nhieu tu:")
dstu = [tu for tu in st.split(" ")]
print("Cac tu co trong chuoi la:")
for i in dstu:
    print(i, end= ' ')
thtu = set(dstu)
print("\nDa loai bo phan tu trung la:")
for i in thtu:
    print(i, end = ' ')
dstu = sorted(list(thtu))
print('\Cac tu da duoc sap xep theo thu tu tu dien la:')
for i in dstu:
    print(i,end = ' ')