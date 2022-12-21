st=input("Nhap chuoi: ")
a,b,c,d,e=0,0,0,0,0
for i in st:
    if i.isdigit(): a=1
    if i == i.lower(): b=1
    if i == i.upper(): c=1
    if i=="$" or i=="#" or i=="@": d=1
    if len(st)>=6 and len(st)<=12: e=1

if a==1 and b==1 and c==1 and d==1 and e==1:
    print("hop le")
else: print("ko hop le")