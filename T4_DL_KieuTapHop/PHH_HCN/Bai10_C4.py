#Bài 10_Chương 4
print("Nhập dữ liệu vào (Dừng khi nhập \"exit\" hoặc Ctrl-Z):")
contents = []
while True:
    try:
        line = input()
        if (line == "exit"):
        	break
    except EOFError:
        break
    contents.append(line)
for i in range(0, len(contents)):
	contents[i] = contents[i].split(",")
	if len(contents[i]) != 3:
		print("Có lỗi xảy ra, vui lòng kiểm tra dữ liệu nhập")
		quit()
	contents[i] = tuple(contents[i])
print("Trước khi sắp xếp: ", contents)
print("Sau khi sắp xếp: ", sorted(contents))