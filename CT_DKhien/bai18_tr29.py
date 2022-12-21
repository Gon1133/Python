import math

n=int(input("nhap so nguyen: "))
e=1.0
for i in range(1,n+1):
    e = e + 1/(math.factorial(i))
print("e =",e)
