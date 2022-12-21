st=input("Nhập vào chuỗi bất kỳ: ")
dc, ds = 0, 0
for kt in st:
    if kt.isalpha():
        dc += 1
    elif kt.isdigit():
        ds += 1
print("So chu cai la:",dc)
print("So chu so la: ", ds)

