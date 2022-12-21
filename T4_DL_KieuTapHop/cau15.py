dic = {}
while True:
    ta = input("Nhap English:")
    if ta != '':
        tv = input("Nhap Vietnamese:")
        dic[ta]=tv
    else:
        break
print("Cac tu co trong tu dien",dic)
tu = input("Ban muon tra tu: ")
try:
    print("Nghia tieng viet cua:",tu,"la",dic[tu])
except KeyError:
    print("Tu nay kh co trong tu dien")


