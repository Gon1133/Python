ht=input("Nhap vao ho ten:")
print("Ho ten vua nhap la:",ht)
ht=ht.strip()
i=1
while i<len(ht)-1:
    if ht[i]==' ' and ht[i+1]==' ':
        ht=ht[:i]+ht[i+1:]
    else: i+=1
print("Ho ten sau khi bo khoang trang thua la:",ht)
kt=input("Nhap ky tu can kiem tra:")
if ht.find(kt)!=-1:
    print("Co ky tu",kt,"trong ho ten")
else:
    print("Khong co ky tu",kt,"trong ho ten")
ktd=ht.find(' ')
ho=ht[:ktd]
ktc=ht.rfind(' ')
ten=ht[ktc+1:]
print("nguoi nay co ho la",ho,"va co ten la",ten)