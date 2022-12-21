def GiaiThua(n):
	kq=1
	for i in range(1,n+1):
		kq=kq*i
	return kq
n=int(input("Nhập số nguyên dương n = "))
print(n,"! =",GiaiThua(n))