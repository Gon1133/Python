old_list=[1,2,5,8,10]
print(old_list)
new_list=(x**2 for x in old_list if x%2==0)
for ob in new_list:
    print(ob, end=" ")