a = int(input('nhập số nguyên dương: '))
dem=0
for i in range(1,a+1):
    if a % i == 0:
        dem += 1
print('có',dem,'ước số của',a)