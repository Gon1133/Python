import random

a=int(input("nhap a: "))
b=int(input("nhap b: "))

list1=random.sample(range(a,b+1),5)
print("list1 = ",list1)


list2 = random.sample([x for x in range(a,b+1) if x%2==0],10)
print("list2 = ",list2)

k=int(input("nhap k: "))
list3 = random.sample([x for x in range(a,b+1) if x%5==0 and x%7==0],k)
print("list3 = ",list3)

list4 = random.shuffle(list3)
print("list4 = ",list4)