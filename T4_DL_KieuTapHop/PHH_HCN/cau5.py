a = int(input("UP "))
b = int(input("DOWN "))
c = int(input("LEFT "))
d = int(input("RIGHT "))
ds=[a-b,c-d]
print((ds[0]**2+ds[1]**2)**0.5)