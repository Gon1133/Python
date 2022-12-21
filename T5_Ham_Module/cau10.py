def DsCB2():
	n=int(input("Nhap so n: "))
	ds=[x**0.5 for x in range(1,n)]
	print("List cac ptu can bac 2:",ds)

def DsCB3():
	n=int(input("Nhap so n: "))
	m=int(input("Nhap so m: "))
	ds=[x**(1/3) for x in range(1,n)]
	print("in",m,"ptu trong List cac ptu can bac 3 :",ds[:m])

def TupleLP():
	n=int(input("Nhap so n: "))
	m=int(input("Nhap so m: "))
	ds=[x**3 for x in range(1,n)]
	tup=tuple(ds)
	print("in Tuple Lap Phuong:",tup[-m:])

def TupBP():
	n=int(input("Nhap so n: "))
	m=int(input("Nhap so m: "))
	k=int(input("Nhap so k: "))
	ds=[x**2 for x in range(1,n)]
	tup=tuple(ds)
	print("in Tuple Binh Phuong:",tup[k:k+m])

