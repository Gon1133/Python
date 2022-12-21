print("TẠO TỪ ĐIỂN")
dictionary={}
while True:
    key = input("Nhap key: ")
    if key == "0":
        break
    value = input("Nhap value cua \""+str(key)+"\": ")
    if key != "" and value != "":
        dictionary[key] = value
print("từ điển vừa tạo:",dictionary)
print("TRA TỪ ĐIỂN")
if len(dictionary)!=0:
    while True:
        key_in = input("nhap khoa can tra: ")
        if key_in == "0": break
        if key_in in dictionary:
            print("Nghia tuong ung la: ", dictionary[key_in])
else: print("Từ điển rỗng")