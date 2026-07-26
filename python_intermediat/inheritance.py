# What is Inheritance?

# Definition
# Inheritance is the process by which one class acquires the properties and methods of another class.

# Simply put:
# Instead of writing the same code again, we reuse it.
class Human :
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender 

    def eat(self):
        print(f"the {self.name} is eating.....")

    def sleep(self):
        print(f"the {self.name} is sleeping....")
    def whoami(self):
         print("hello i am a humman ::::")
    def __str__(self):
        return f'the name is {self.name} and age is {self.age} is a {self.gender}'

class Student(Human) :
    def __init__(self ,name ,age ,gender , roll ,bg,attendens):
        super().__init__(name,age,gender)
        self.roll = roll 
        self.blood_group  = bg 
        self.attendens = attendens 

    def __str__(self):
            text = super().__str__()
            text += " | roll {} , blood group {} , attendens {}%".format(
                self.roll, self.blood_group, self.attendens
            )
            return text
    def whoami(self):
        super().whoami()
        print("and i am a student also ")
        

human1 = Human("shivasai",12,"M")
print(human1.age)
print(human1.gender)
human1.eat()

stu1 = Student("shivasai",90,"G",11,"b+",20)
print(stu1.name)
stu1.eat()
print(human1.name) 

stu2 = Student("karthikeya ",20,"W",17,"o+",100)

stu2.eat()
print(human1)
print(stu2)
human1.whoami()
stu2.whoami()