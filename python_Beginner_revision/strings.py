# strings sequence of charactrer 
# we slice the string and assing 
text = "Hello World "

# text[2] = "shiva"
# print(text)  error 

print(text[::-1])


print(len(text))


age = int (input( "enter the age : "))
name = input("enter the name : ")

print("my name is %s and my age is %d" % (name, age))
print("my name is {} and my age is {}".format(name, age))
print(f"my name is {name} and  my age is {age} ")
text = "Hello world "
print(text.upper())
print(text.lower())
print(text.title())
print(text.swapcase())
print(text.isupper())
print(text.islower())
