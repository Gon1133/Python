import math
def UCLN(a,b):
    if a % b == 0: return b
    if b % a == 0: return a
    if a>b: return UCLN(a-b,b)
    else: return UCLN(a,b-a)

class Fraction:
    def __init__(self, tu=0, mau=0):
        self.ts=tu
        self.ms=mau
    def Nhap(self):
        self.ts=int(input("Nhập tử số: "))
        while self.ms == 0:
            self.ms=int(input("Nhập mẫu số: "))
    def In(self):
        if self.ms<0:
            print("Phân số = -%d/%d" %(self.ts,abs(self.ms)))
        elif self.ts==0:
            print("Phân số = 0")
        elif self.ms==1:
            print("Phân số = %d" %self.ts)
        else: print("Phân số = %d/%d" %(self.ts,self.ms))

    def TuSo(self):
        return self.ts
    def MauSo(self):
        return self.ms

    def PSoND(self):
        print("%d/%d" %(self.ms,self.ts))

    def GTThuc(self):
        return float(self.ts/self.ms)

    def ToiGian(self):
        ts = self.ts / UCLN(self.ts,self.ms)
        ms = self.ms / UCLN(self.ts,self.ms)
        print("%d/%d" %(ts,ms))

    def SoSanhPSo(self,PhanSo):
        if self.ts * PhanSo.ms > self.ms * PhanSo.ts:
            print("%d/%d > %d/%d" %(self.ts,self.ms,PhanSo.ts,PhanSo.ms))
        if self.ts * PhanSo.ms == self.ms * PhanSo.ts:
            print("%d/%d = %d/%d" %(self.ts,self.ms,PhanSo.ts,PhanSo.ms))
        if self.ts * PhanSo.ms < self.ms * PhanSo.ts:
            print("%d/%d < %d/%d" %(self.ts,self.ms,PhanSo.ts,PhanSo.ms))

    def Cong2PSo(self,PhanSo):
        if self.ms != PhanSo.ms:
            ts = self.ts * PhanSo.ms + self.ms * PhanSo.ts
            ms = self.ms * PhanSo.ms
        else:
            ts = self.ts + PhanSo.ts
            ms = self.ms
        print("Tong 2 phan so = %d/%d" %(ts,ms))

    def Tru2PSo(self,PhanSo):
        if self.ms != PhanSo.ms:
            ts = self.ts * PhanSo.ms - self.ms * PhanSo.ts
            ms = self.ms * PhanSo.ms
        else:
            ts = self.ts - PhanSo.ts
            ms = self.ms
        print("Hieu 2 phan so = %d/%d" %(ts,ms))

    def Nhan2PSo(self,PhanSo):
        ts = self.ts * PhanSo.ts
        ms = self.ms * PhanSo.ms
        print("Tich 2 phan so = %d/%d" %(ts,ms))

    def Chia2PSo(self,PhanSo):
        ts = self.ts * PhanSo.ms
        ms = self.ms * PhanSo.ts
        print("Thuong 2 phan so = %d/%d" %(ts,ms))

PhanSo1 = Fraction()
print("Nhap phan so thu nhat:")
PhanSo1.Nhap()
PhanSo1.In()
PhanSo2 = Fraction()
print("Nhap phan so thu hai:")
PhanSo2.Nhap()
PhanSo2.In()

print("Tu so cua phan so thu nhat =",PhanSo1.TuSo())
print("Mau so cua phan so thu hai =",PhanSo2.MauSo())

print("Nghich dao cua phan so thu nhat =",end=" ")
PhanSo1.PSoND()

print("Gia tri thuc cua phan so thu nhat =",PhanSo1.GTThuc())

print("Toi gian cua phan so thu hai =",end=" ")
PhanSo2.ToiGian()

PhanSo1.SoSanhPSo(PhanSo2)

PhanSo1.Cong2PSo(PhanSo2)
PhanSo1.Tru2PSo(PhanSo2)
PhanSo1.Nhan2PSo(PhanSo2)
PhanSo1.Chia2PSo(PhanSo2)