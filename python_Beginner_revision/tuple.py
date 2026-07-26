# x = (12,13,4,5,1,2,431,4,1,43,1,1,1,1,12)
# print(x[1]==18)
# # sets os also a stack 
# s = {1,2,3,1,2,12,3,1,21,1}
# print(s)
# s.add(32)
# print(s)
# print(s.pop())




dicts = {
    'name' : "shivasai",
    "age" : 12 ,
    "class" : "CSBS",
    'roll' : 23421
}
print(dicts["age"])

#  items , keys , values 

dicts.items()
dicts.keys()
dicts.values()
# membership operaters ;
#  "in"  and "not in "

print("age" in dicts)
"name" not in dicts

# identical operater 
#  "if" and 'is' and "is not "

type(dicts["age"]) is int 
dicts["name"] is "shivasai"



