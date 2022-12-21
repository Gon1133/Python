import math
class Toado:
    '''Lớp tọa độ gồm 2 thuộc tích và 6 phương thức'''
    def __init__(self, hd=0, td=0):
        self.x = hd
        self.y = td
    def Nhap(self):
        self.x = float(input("Nhap hoanh do: "))
        self.y = float(input("Nhap tung do: "))
    def Xuat(self):
        print('(',self.x,',',self.y,')')
    def Hoanhdo(self):
        return self.x
    def Tungdo(self):
        return self.y
    def Khoangcach(self, ob):
        kc = math.sqrt(pow(ob.x-self.x,2)+pow(ob.y-self.y,2))
        return kc
A=Toado(2,3)
print("Diem A co toa do la:")
A.Xuat()
B=Toado()
print("Diem B co toa do la:")
B.Xuat()
print("Nhap toa do cho A:")
A.Nhap()
print("Diem A co toa do la:")
A.Xuat()
print("Nhap toa do cho B:")
B.Nhap()
print("Diem B co toa do la:")
B.Xuat()
C=Toado()
print("Nhap toa do cho C:")
C.Nhap()
print("Hoanh do cua C la:",C.Hoanhdo())
print("Tung do cua C la:",C.Tungdo())
kcAB = A.Khoangcach(B)
print("Khoang cach tu A den B la:",kcAB)
kcAC = A.Khoangcach(C)
print("Khoang cach tu A den C la:",kcAC)
kcBC = B.Khoangcach(C)
print("Khoang cach tu B den C la:",kcBC)
if kcAB+kcAC > kcBC and kcAB+kcBC > kcAC and kcAC+kcBC > kcAB:
    print("3 diem A,B,C tao thanh 1 tam giac")
else:
    print("3 diem A,B,C khong tao thanh tam giac")
