mylist = [1,2,3,4,10,"shivsai",True,8.913]

print(type(str(int(mylist[6]))))
print(mylist[1:4])
for x in mylist :
    print(x)
mylist.append(12)
print(mylist)

anotherlist = [0 , 9,832,19]
mylist.append(anotherlist)
print(mylist * 2)
print(len(mylist))
print(max(anotherlist))
print(min(anotherlist))
mylist.insert(6,"karthik")
print(mylist)
mylist.remove(2)
print(mylist)
mylist.pop(6)
print(mylist)
print(mylist.index("karthik"))
anotherlist.sort()
print(anotherlist)