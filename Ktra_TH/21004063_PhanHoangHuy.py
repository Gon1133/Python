class Laodong:
    def __init__(self, ma="2100", ht="hoang huy", lhd="thoi vu"):
        self.ma = ma
        self.ht = ht
        self.lhd = lhd
    def nhap(self):
        self.ma = input("Nhap ma nhan vien: ")
        self.ht = input("Nhap ho ten: ")
        while self.lhd != "lao động thời vụ" and self.lhd != "công nhân chính thức":
            self.lhd = input("Nhap loai hop dong: ")
    def xuat(self):
        print("ma so nhan vien:",self.ma)
        print("ho ten:",self.ht)
        print("loai hop dong:",self.lhd)

class LDThoiVu(Laodong):
    def __init__(self, ma="2100", ht="hoang huy", lhd="thoi vu",SoNgayCong=21, DonGiaNgayCong=1000):
        super().__init__(ma, ht, lhd)
        self.snc = SoNgayCong
        self.dgnc = DonGiaNgayCong
    def nhapLDThoiVu(self):
        Laodong.nhap(self)
        while self.lhd != "lao động thời vụ":
            self.lhd = input("nhap loai hop dong: ")
        self.snc =  int(input("Nhap so ngay cong: "))
        self.dgnc = int(input("Nhap Don gia ngay cong: "))
    def xuatLDThoiVu(self):
        Laodong.xuat(self)
        print("So ngay cong:",self.snc)
        print("Dong gia ngay cong:",self.dgnc)

    def TinhLuong(self):
        if self.snc >= 25:
            return self.snc * self.dgnc + 2500000
        else:
            return self.snc * self.dgnc

class CNChinhThuc(Laodong):
    def __init__(self, ma="2100", ht="hoang huy", lhd="thoi vu", ThamNienCT=10, HeSoLuong=1.2):
        super().__init__(ma, ht, lhd)
        self.tnct = ThamNienCT
        self.hsl = HeSoLuong
    def nhapCNChinhThuc(self):
        Laodong.nhap(self)
        while self.lhd != "công nhân chính thức":
            self.lhd = input("nhap loai hop dong: ")
        self.tnct = float(input("Nhap tham nien CT: "))
        self.hsl = float(input("Nhap he so luong: "))
    def xuatCNChinhThuc(self):
        Laodong.xuat(self)
        print("Tham nien CT:",self.tnct)
        print("He so luong:",self.hsl)

    def TinhLuong(self):
        lcb=1050000
        if self.tnct >= 3:
            pc = lcb * 1.2
        else:
            pc = lcb * 1
        return lcb * self.hsl + pc


nv = Laodong()
nv.nhap()
nv.xuat()
print()


print("Nhap thong tin LDThoiVu")
nv1 = LDThoiVu()
nv1.nhapLDThoiVu()
nv1.xuatLDThoiVu()
print("Luong LD thoi vu vua nhap:",nv1.TinhLuong())

nv2 = CNChinhThuc()
print("Nhap thong tin CNChinhThuc")
nv2.nhapCNChinhThuc()
nv2.xuatCNChinhThuc()
print("Long CN ChinhThuc vua nhap:",nv2.TinhLuong())