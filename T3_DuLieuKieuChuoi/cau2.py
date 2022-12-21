st = input("Nhap chuoi:")
for i in st:
    if i.isdigit() == False:
        st=st.replace(i,"")
print("chuoi sau khi xu ly:",st)
