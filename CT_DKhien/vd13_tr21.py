n=int(input("Nhập N: "))
for i in range(1,n):
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            print(i,"la hop so")
            break
        else: print(i,"la so nguyen to")