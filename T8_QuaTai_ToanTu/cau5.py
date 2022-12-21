from datetime import date
import datetime

class Sinhvien:
    truong = "VLUTE"
    def __init__(self, mssv="21004063", ht="Phan Hoang Huy", ns=date(2003,8,14),dtb=8):
        self.mssv = mssv
        self.ht = ht
        self.ngaysinh = ns
        self.dtb = dtb

    def nhap(self):
        self.mssv = input("Nhap ma so sinh vien: ")
        self.ht = input("nhap ho ten: ")
        ngay = int(input("Nhap ngay sinh: "))
        thang = int(input("Nhap thang sinh: "))
        nam = int(input("Nhap nam sinh: "))
        self.ngaysinh = date(nam, thang, ngay)
        self.dtb = int(input("Nhap diem trung binh: "))

    def xuat(self):
        print("Truong:",self.truong)
        print("Ma so sinh vien:",self.mssv)
        print("Ho:",self.Ho())
        print("Tuoi:",self.Tuoi())
        print("Diem trung binh:",self.dtb)

    def Tuoi(self):
        return datetime.datetime.now().year - self.ngaysinh.year

    def Ho(self):
        for i in range(len(self.ht)):
            if self.ht[i] == " ":
                return self.ht[:i]

    def __add__(self,n):
        dtb = self.dtb + n
        return Sinhvien(dtb = dtb)

class SinhvienIT(Sinhvien):
    khoa = "FIT"
    def __init__(self, qq="Vinh Long"):
        super().__init__(mssv="21004063", ht="Phan Hoang Huy", ns=date(2003, 8, 14), dtb=8)
        self.qq = qq

    def nhapIT(self):
        self.nhap()
        self.qq = input("nhap que quan: ")

    def xuatIT(self):
        self.xuat()
        print("que quan:",self.qq)

    def __nhohon__(self, sv):
        if self.dtb < sv.dtb: return True
        else: return False


n=0
while n<=0 or n>99:
    n=int(input("nhap so luong SvIT: "))
listIT=[]
for i in range(n):
    print("nhap sinh vien IT thu", i + 1)
    sv=SinhvienIT()
    sv.nhapIT()
    listIT.append(sv)

for i in listIT:
    print("\nthong tin sinh vien IT thu", i+1)
    i.xuatIT()

count=0
for i in range(n):
    if listIT[i].qq == "Vinh Long":
       count+=1
print("\nco %d SV IT song o Ving Long" %count)

for i in range(n-1):
    for j in range(i+1,n):
        if listIT[i].dtb < listIT[j].dtb:
            listIT[i].dtb,listIT[j].dtb = listIT[j].dtb,listIT[i].dtb
print("\nds SV IT sau khi sap xep:")
for i in listIT:
    print("\nthong tin sinh vien IT thu", i+1)
    i.xuatIT()
