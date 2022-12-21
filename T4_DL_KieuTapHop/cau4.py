import math
u = int(input("Up="))
d = int(input("Down="))
l = int(input("Left:"))
r = int(input("Right:"))
ds=[(u-d),(l-r)]
kc=float(pow((pow(ds[0],2)+pow(ds[1],2)),0.5))
print("Khoảng cách cần tìm:",kc)
math.sqrt(kc)