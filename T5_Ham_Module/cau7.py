def A(n):
	if n==0: return 0
	else: return A(n-1) + 1/n

def B(n):
	if n <= 0: return 1
	else: return B(n-3)+10

def C(n):
	if n==1 or n==2: 
		return 1
	else: 
		return C(n-1)+C(n-2)

n=int(input("Nhap so nguyen duong: "))
print(A(n))
print(B(n))
print(C(n))