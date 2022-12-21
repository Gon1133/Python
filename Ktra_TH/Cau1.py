from random import randint
#Nhập chuỗi
st = input("Nhập vào chuỗi bất kì: ")
#In chuỗi
print("Chuỗi vừa nhập là: ", st)
#Cho biết kí tự kt xuất hiện bao nhiêu lần
kt = input("Nhập vào kí tự kt: ")
while len(kt) != 1:
	kt = input("Nhập vào kí tự kt: ")
#Đếm số lần xuất hiện
count = 0
for i in range(0, len(st)):
	if st[i] == kt:
		count += 1
print("Số lần xuất hiện của '%s' là: %d"%(kt, count))
#Cho biết chữ số nào xuất hiện nhiều nhất trong chuỗi
temp = []
for i in range(0, 10):
	temp.append(st.count(str(i)))
xhmax = max(temp)
print("Các chữ số xuất hiện nhiều nhất là: ", end="")
if xhmax == 0:
	print("Không có chữ số nào xuất hiện trong chuỗi")
else:
	for k in range(0, len(temp)):
		if temp[k] == xhmax:
			print(k, end="")
#Chọn và in ra 1 từ ngẫu nhiên có trong chuỗi
list_st = st.split()
ngaunhien = randint(0, len(list_st)-1)
print("Một từ ngẫu nhiên trong chuỗi là: ", list_st[ngaunhien])
#Cho biết trong chuỗi có bao nhiêu từ có đúng 3 ký tự
count = 0
for i in range(0, len(list_st)):
	if len(list_st[i]) == 3:
		count += 1
print("Có %d từ có đúng 3 ký tự trong chuỗi"%count)