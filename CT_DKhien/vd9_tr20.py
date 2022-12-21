n = int(input('nhập mệnh giá tiền: '))
print('các phương án đổi tiền (2,3,5) là:')
for i in range (n//2+1):
    for j in range(n // 3 + 1):
        for k in range(n // 5 + 1):
            if (i*2+j*3+k*5==n):
                print('(',i,',',j,',',k,')')