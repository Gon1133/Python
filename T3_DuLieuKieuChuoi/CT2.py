st=input("Nhap vao chuoi bat ki: ")
print("Chuoi vua nhap la: ",st)
st=st.upper()
print("Chuoi sau khi doi la:",st)
st=st.replace(' ','-')
print("Chuoi sau khi thay the la:",st)
a=st.split('-')
dem=0
print("cac tu co trong chuoi la:")
for i in a:
    if i!='':
        dem += 1
        print(i)
print("Trong chuoi co",dem,"tu")