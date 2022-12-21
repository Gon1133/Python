# from collections import Counter
class Document:
    truong="ĐH.SPKT Vĩnh Long"
    def __init__(self,tentailieu=0,tenchubien=0,namxuatban=0,sotrang=0):
        self.tl = tentailieu
        self.cb = tenchubien
        self.nxb = namxuatban
        self.st = sotrang
    def Nhap(self):
        self.tl = input("Nhap ten tai lieu: ")
        self.cb = input("Nhap ten chu bien: ")
        while self.nxb>2022 or self.nxb<=0:
            self.nxb = int(input("Nhap nam xuat ban: "))
        while self.st<10 or self.st>500:
            self.st = int(input("Nhap so trang: "))
    def In(self):
        print("Truong:",self.truong)
        print("Ten tai lieu:",self.tl)
        print("Ten chu bien:",self.cb)
        print("Nam xuat ban:",self.nxb)
        print("So trang:",self.st)

    def TTL(self):
        return self.tl
    def TCB(self):
        return self.cb
    def NXB(self):
        return self.nxb
    def ST(self):
        return self.st

    def SSST(self,tailieu):
        if self.st>tailieu.st: return 1
        elif self.st<tailieu.st: return -1
        else: return 0

# tailieu1 = Document()
# print("Nhap thong tin cua tai lieu thu nhat")
# tailieu1.Nhap()
# tailieu1.In()
# tailieu2 = Document()
# print("Nhap thong tin tai lieu thu hai")
# tailieu2.Nhap()
# tailieu2.In()
#
# print("ten tai lieu thu nhat:",tailieu1.tl)
# print("ten chu bien thu nhat:",tailieu1.cb)
# print("nam xuat ban tai lieu thu nhat:",tailieu1.nxb)
# print("so trang tai lieu thu nhat:",tailieu1.st)
#
# if tailieu1.SSST(tailieu2) == 1: print("so trang tai lieu 1 > so trang tai lieu 2")
# elif tailieu1.SSST(tailieu2) == -1: print("so trang tai lieu 1 < so trang tai lieu 2")
# else: print("so trang tai lieu 1 = so trang tai lieu 2")

N=[]
while True:
    i=0
    i=int(input("Nhap thu tu cua tai lieu (thoat khi nhap 0): "))
    if i==0: break
    tailieu=Document()
    print("Nhap thong tin tai lieu thu %d" %i)
    tailieu.Nhap()
    N.append(tailieu)
print("Danh sach tai lieu vua tao")
for i in N:
    i.In()

# dem tai lieu co so trang > 300
dem=0
for i in N:
    if i.st > 300: dem+=1
print("so tai lieu co hon 300 trang =",dem)

# cho biet chu bien co nhieu tai lieu nhat
t=N[0].cb
print(N.count(t))