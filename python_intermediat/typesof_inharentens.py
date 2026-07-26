"""
so types of inharitence :

1. single inharients
2. multtiple inharitance
3. multi-level inharitance 
4. herical inharitance 
5. hybride inharitance 


"""

# multiple inharitance 

# One child class inherits from more than one parent class.

#  Parent1      Parent2
#       \       /
#        \     /
#         Child

class Father :
    def money(self):
        print("father has money ..\n")
class Mother :
    def love(self):
        print("mother shows love to words kids ..\n")
class Child(Father,Mother) :
    def eat(self):
        print('the child is eating \n')

child1 = Child()
child1.money()
child1.love()
child1.eat()

# 3. Multilevel Inheritance
# Definition

# A child inherits from a parent, and another child inherits from that child.

# Grandparent
#       │
#       ▼
#    Parent
#       │
#       ▼
#     Child

class Animal :
    def eat(self):
        print("the animal is eating \n")
class Dog(Animal):
    def bark(self):
        print("dog always barks...\n")
class Puppy(Dog):
    def woff(self):
        print("puppy always woffs...\n")

puppy1 = Puppy()
dog = Dog()
Animal1 = Animal()
puppy1.woff()
puppy1.bark()
puppy1.eat()
dog.eat()
dog.bark()
Animal1.eat()


# 4. Hierarchical Inheritance
# Definition

# Multiple child classes inherit from the same parent.

#         Parent
#        /   |   \
#       ▼    ▼    ▼
#    Child1 Child2 Child3

class Human :
    def eat(self):
        print("the person is eating....\n")
    def sleep(self):
        print("the person is sleeping....\n")
class Student(Human):
    def study(self):
        print("the student is studing....\n")
class Teacher(Human):
    def teach(self):
        print("the teacher is teachig class \n")

teacher1 = Teacher()
student1 = Student()
teacher1.eat()
teacher1.teach()
student1.sleep()
student1.study()

# 5. Hybrid Inheritance
# Definition

# Hybrid inheritance is a combination of two or more inheritance types.

# For example:

#           A
#         /   \
#        ▼     ▼
#        B     C
#         \   /
#           ▼
#           D

class A:
    def showA(self):
        print("Class A")


class B(A):
    def showB(self):
        print("Class B")


class C(A):
    def showC(self):
        print("Class C")


class D(B, C):
    def showD(self):
        print("Class D")


obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()