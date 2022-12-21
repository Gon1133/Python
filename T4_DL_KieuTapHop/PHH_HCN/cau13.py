str=input("Nhap chuoi: ")
str = str.split()
set = set(str)
set = sorted(set)
str = ""
for i in range(len(set)):
    if i != len(set)-1:
        str += set[i] + " "
    else:
        str += set[i]
print("chuoi sau khi sap xep:",str)