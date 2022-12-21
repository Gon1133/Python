st=input("Nhap chuoi: ")
for i in range(len(st)):
    if st[i] == "@":
        a=i
st1 = st[:a]
st2 = st[a+1:]
print("username la:",st1)
print("companyname la:",st2)

