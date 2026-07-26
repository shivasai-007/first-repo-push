# Object-Oriented Programming (OOP) in Python
# Step 1: What is OOP?

# Instead of writing everything separately, Python 
# groups the data and actions together. This concept is called Object-Oriented Programming (OOP).

# Definition

# Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, 
# where each object contains data (attributes) and functions (methods).

# what is a class :
# a class is a blueprint or a template of a groups of instances 

class Csbs :
    branch_code = "@cs/43-R22"
    hod = "chomii_bhai"
    classno = 104
    class_striength = 0
    
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender 
        Csbs.class_striength += 1

    def __del__(self):
        print(f"the student {self.name} has been deleted  ")
        Csbs.class_striength -= 1

    def show(self):
        print(f'my name is {self.name},and my age is {self.age}\n gender :{self.gender}')
        # or 
    def __str__(self):
        return f"my name is {self.name},and my age is {self.age}\n gender :{self.gender}"
    def get_older(self,year):
        self.age += year 
    
    def infoclass(self) :
        print(f'branck name {self.branch_code},the hod of the branch is {self.hod}\n namd the room number is {self.classno}')

student1 = Csbs("shivasai",23,'M')
student2 = Csbs("karthikeya",43,"G")
student3 = Csbs("vijju ",3,"G")
print(student1.branch_code)
student1.show()
del student1
print("program is running ")
student2.infoclass()
student2.get_older(6)
result = student2.__str__()
print(result)

print(Csbs.class_striength)
