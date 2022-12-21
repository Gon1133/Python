from datetime import date
class Hocvien:
    tt="CIT"
    def __init__(self, ms="2100", ht="huy", ns=date(2003,8,14), dlt=5.2, dtt=5.1):
        self.ms=ms
        self.ht=ht
        self.ns=ns
        self.dlt=dlt
        self.dtt=dtt

    def nhap(self):
        self.ms = input("Nhap ma so: ")
        self.ht = input("Nhap ho ten: ")
        ngay = int(input("Nhap ngay sinh: "))
        thang = int(input("Nhap thang sinh: "))
        nam = int(input("Nhap nam sinh: "))
        self.ns = date(nam, thang ,ngay)
        self.dlt = float(input("Nhap diem ly thuyet: "))
        self.dtt = float(input("Nhap diem thuc hanh: "))

    def Ten(self):
        ten = self.ht[::-1]
        for i in range(len(ten)):
            if ten[i] == " ":
                ten = ten[:i]
                break
        return ten[::-1]

    def DTB(self):
        return (self.dtt + self.dlt)/2

    def xuat(self):
        print("Trung tam:", self.tt)
        print("ma so:", self.ms)
        print("ho ten:", self.ht)
        print("ngay sinh:", self.ns.strftime("%m/%d/%Y"))
        print("diem trung binh:", self.DTB())

n=int(input("Nhap so hoc vien: "))
listHV=[]
for i in range(n):
    print("Nhap hoc vien thu",i+1)
    hv=Hocvien()
    hv.nhap()
    listHV.append(hv)

for i in range(n):
    if listHV[i].ns.month == 12:
        print(listHV[i].Ten(),end=",")

print()
# dem=0
# for i in range(n):
#     if listHV[i].DTB() >= 5 and listHV[i].dlt >= 5 and listHV[i].dtt >= 5:
#         dem+=1
# print("co %d hoc vien duoc cap chung chi" %dem)