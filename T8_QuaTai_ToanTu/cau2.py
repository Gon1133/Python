from datetime import date
class Connguoi:
    dangdi = 'thẳng'
    trikhon = 'có'

    def __init__(self, md='vàng', mm='đen', nm='AB',
                 qt='Việt Nam', ns=date(1975, 6, 22)):
        self.mauda = md
        self.maumat = mm
        self.nhommau = nm
        self.quoctich = qt
        self.ngaysinh = ns

    def Nhap(self):
        self.mauda = input("Nhập màu da:")
        self.maumat = input("Nhập màu mắt:")
        self.nhommau = input("Nhập nhóm máu:")
        self.quoctich = input("Nhập quốc tịch:")
        ngay = int(input("Nhập ngày sinh:"))
        thang = int(input("Nhập tháng sinh:"))
        nam = int(input("Nhập năm sinh:"))
        self.ngaysinh = date(nam, thang, ngay)

    def Xuat(self):
        print('Dáng đi:', self.dangdi)
        print('Trí khôn:', self.trikhon)
        print('Màu da:', self.mauda)
        print('Màu mắt:', self.maumat)
        print('Nhóm máu:', self.nhommau)
        print('Quốc tịch:', self.quoctich)
        print('Ngày sinh:', self.ngaysinh)
        # print('Ngày sinh:', self.ngaysinh.strftime("%d/%m/%Y"))

    def Mauda(self):
        return self.mauda

    def Maumat(self):
        return self.maumat

    def Sinhnhat(self):
        return self.ngaysinh


    def Namsinh(self):
        return self.ngaysinh.year

    def __add__(self,n):
        ns = self.ngaysinh.day + n
        self.ngaysinh = date(self.ngaysinh.year, self.ngaysinh.month, ns)
        return Connguoi(ns = ns)

    def __sub__(self, n):
        ns = self.ngaysinh.day - n
        self.ngaysinh = date(self.ngaysinh.year, self.ngaysinh.month, ns)
        return Connguoi(ns=self.ngaysinh)

    def __and__(self, ob2):
        if (self.ngaysinh.day == ob2.ngaysinh.day) and (self.ngaysinh.month == ob2.ngaysinh.month):
            return True
        else:
            return False

    def __or__(self, ob2):
        if (self.Maumat() == 'xanh' or ob2.Maumat() == 'xanh'):
            return True
        else:
            return False

    def __xor__(self, ob2):
        if (self.mauda == "trang" and ob2.mauda == "vang") or\
            (self.mauda == "vang" and ob2.mauda == "trang"):
            return True
        else:
            return False

    def __invert__(self):
        if not self.ngaysinh.day == 14:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.Namsinh() > other.Namsinh():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.Namsinh() >= other.Namsinh():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.ngaysinh.month < other.ngaysinh.month:
            return True
        else:
            return False

    def __le__(self, other):
        if self.ngaysinh.month <= other.ngaysinh.month:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.ngaysinh == other.ngaysinh:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.ngaysinh != other.ngaysinh:
            return True
        else:
            return False

P1 = Connguoi()
P1.Nhap()
print('Thông tin về P1:')
P1.Xuat()
P2 = Connguoi()
P2.Nhap()
print('Thông tin về P2:')
P2.Xuat()

P1.__add__(6)
print("\nngay sinh sau khi cong:")
P1.Xuat()

P1.__sub__(6)
print("\nngay sinh sau khi tru:")
P1.Xuat()

if(P1.__and__(P2) == True):
    print('Hai người cùng sinh nhat')
else:
    print('Hai người KHÔNG cùng sinh nhat')

if(P1.__or__(P2) == True):
    print('Có ít nhất 1 người có mat mau xanh')
else:
    print('Cả 2 người đều KHÔNG có mat mau xanh')

if(P1.__xor__(P2) == True):
    print("co 1 nguoi da trang va 1 nguoi da vang")
else:
    print("khong co co 1 nguoi da trang va 1 nguoi da vang")

if(P1.__invert__() == True):
    print('Người này KHÔNG trung sinh nhat voi toi')
else:
    print('Người này trung sinh nhat voi toi')

if P1.__xor__(P2) == True:
    print("1")
else: print("2")
