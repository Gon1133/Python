def Info(num_1, *num_n):
    print(num_1,end=" ")
    for i in num_n:
        print(i,end=" ")
Info(1)
Info(1,2)
Info(1,2,3)
Info()