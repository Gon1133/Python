from random import randint
# cau1
s=input("Nhap chuoi bat ky: ")
print("chuoi vua nhap:",s)

# kt xuat hien bao nhieu lan
kt = input("Nhap ky tu kt: ")
count = 0
for i in range(0, len(s)):
    if s[i] == kt:
        count += 1
print("Số lần xuất hiện của '%s' là: %d"%(kt, count))

# ky tu nao xuat hien nhieu nhat trong chuoi
a=[]
for i in range(10):
    a.append(s.count(str(i)))
csmax = max(a)
print("cac chu so xuat hien nhieu nhat la: ",end="")
if csmax==0:
    print("khong chu so nao xuat hien")
else:
    for i in range(len(a)):
        if a[i] == csmax:
            print(i, end=" ")

print()
# in 1 tu ngau nhien
s2 = s.split()
ran = randint(0, len(s2)-1)
print("Mot tu ngau nhien trong chuoi la:", s2[ran])


# co bao nhieu tu dung 3 ky tu
dem=0
for i in range(len(s)):
    if len(s[i]) == 3:
        dem+=1
print("co %d tu co dung 3 ky tu" %dem)

