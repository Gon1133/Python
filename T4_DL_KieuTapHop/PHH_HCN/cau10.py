print("Nhap du lieu vao")
list=[]
while True:
    x=input()
    if x=="0": break
    list.append(x)
for i in range(len(list)):
    list[i]=list[i].split(",")
    if len(list[i]) > 3:
        print("kiem tra du lieu nhap")
        quit() # ket thuc CT
    list[i] = tuple(list[i])
print("trước khi sắp xếp:",list)
print("sau khi sap xep:",sorted(list))
