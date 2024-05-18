#class abd object


#oops concept

#Class & object

#Class --> A class is a blueprint  or serves as a template 
    #from which individual object are created 

#Object --> Object is sn instance of a class which consists 
    #methods and Properties
 
"""
class demo():
    pass

a = 10
print(type(a))
print(type(demo))
swift = demo()
#print(isinstance(swift,demo))
#print(isinstance(a,int))
print(type(swift))

"""

#class Attributes
"""
class student():
    name = "Ram Kumar"
    age = 25

#getattr method
print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender',"no such attribute found"))
"""
#Dot Notation
"""

print(student.name)
print(student.age)

student.city = "chennai"
print(student.city)
print(student.__dict__)

#del
del student.gender


#setattr

setattr(student,'name','Tutor joes')
print(student.name)

print(student.__dict__)

delattr(student,"city")

setattr(student,'gender','male')

print(student.gender)
print(student.__dict__)

"""


#class Methods

#don't use the object we can call the function easily

class students:
    name = "Kamesh Kumar"
    age = 23

    def printall():
        print("Name : ",students.name)
        print("Age :",students.age)

students.printall()
print(students.__dict__)



#Instance Methods


class students:
    name = "Kamesh Kumar"
    age = 23

    def printall(self,gender):
        print("Name : ",students.name)
        print("Age :",students.age)
        print("Gender :",gender)

obj = students()
obj.printall("Male")
students.printall(obj,"FeMale")


#Constructor __init__ method 


class User:
    def __init__(self):
        print("Call When New Instance Created")

obj = User()



#Property Decorator

"""
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
       # self.msg = self.name + " is " + str(self.age)  + " years old"
    
    @property
    def msg(self):
        return self.name + " is " + str(self.age)  + " years old"


obj = user("KameshKumar",23)
print(obj.name)
print(obj.age)
print(obj.msg)
obj.age = 45
print(obj.msg)

"""

#property Method
"""
class students:
    def __init__(self,total):
        self._total = total 
    
    def average(self):
        return self._total /5.0
    
    def getter(self):
        return self._total
    
    def setter(self,t):
        if t < 0 or t >500:
            print("invalid Total and Can't Change")
        else:
            self._total = t

    total = property(getter,setter)


a = students(450)
print(a.total)
print(a.average())
a.total = 50
print(a.total)
print(a.average())

"""
# class method Decorator
"""
class students:
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        students.count +=1

    def printDetails(self):
        print("Name :",self.name,"  age : ",self.age  )
    
    @classmethod
    def total(cls):
        return cls.count
    

a = students("Kamesh",23)
a.printDetails()
print(a.total())
o = students("kumar",24)
o.printDetails()
print(a.total())

print("Total Admisiion : ",students.total())

"""

#static methods
"""
class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printDetails(self):
        print("Name : ",self.name," Age : ",self.age)

    @staticmethod
    def welcome():
        print("Welcome to Our Institution")

obj = students("kamesh", 23)
obj.printDetails()
obj.welcome()

"""

#Date Abstraction Examole = TV
#         it refer to providing only essential information
# to the outside world and hiding their background details

#         to represents the needed information in program
# without presenting the details


 
#Encapsulation Example tipu tablet
#         it is a process of wrapping code and data together
# into a single unit 


class library:
    def __init__(self,books):
        self.books = books
    
    def list_books(self):
        print("Available books")
        for books in self.books:
            print(books)
    
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("Get your Book now")
            self.books.remove(borrow_book)
        else:
            print("book not Available")
        
    def receive_book(self,receive_book):
        print("you have returned the book")
        self.books.append(receive_book)

books = ["python","C","c++"]
o = library(books)


msg = """
    1.Display books
    2.Borrow books
    3.Return books
"""

while True:
    print(msg)
    ch = int(input("Enter Your choice : "))
    if ch==1:
        o.list_books()
    elif ch==2:
        book = input("Enter Book Name to Borrow : ")
        o.borrow_book(book)
    elif ch==3:
        book = input("Enter Book Name to Return : ")
        o.receive_book(book)
    else:
        print("Thank You come Again")
        quit()


#Single Inheritance
# it is defined as the inheritance in which a derived class
# is inherited from the only one base class
 

"""
class brands:
    brandname1 = "Facebook"
    brandname2 = "youtube"
    brandname3 = "Amazon"

class product(brands):
    product1 = "SocialMedia"
    product2 = "Enterinment"
    product3 = "Shopping"

obj = product()
print(obj.brandname1,"ia a",obj.product1)
print(obj.brandname2,"ia a",obj.product2)
print(obj.brandname3,"ia a",obj.product3)

"""
#muliple inheritance
#it is a feature of object oriented concept where a class
# can inherit properties of more thanm one parent class
"""
class Father:
    def fishing(self):
        print("fishing in Rivers")

    def chess(self):
        print("Playing Chess From Father")


class Mother:
    def cooking(self):
        print("cooking Food")

    def chess(self):
        print("Playing Chess From Mother")


class son(Mother,Father):
    def ride(self):
        print("Riding Bicycle")

obj = son()
obj.ride()
obj.fishing()
obj.cooking()
obj.chess()
obj.chess()

"""
#Multilevel Inheritances
"""
class GrandFather:
    def ownHouse(self):
        print("Grandpa House")

class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")

class son(Father):
    def ownbook(self):
        print("son Have a Book")

obj = son()
obj.ownbook()
obj.ownHouse()
obj.ownBike()

"""

# Handling Diamond Problem (Hybrid inheritances)

"""

class A:
    def display(self):
        print("I am the display of class A")

class B(A):
    def display(self):
         print("I am the display of class b")

class C(A):
    def display(self):
         print("I am the display of class c")

class D(B,C):
    def display(self):
        print("I am the display of class D")

o = D()
o.display()

"""

# operator overloading in polymaorphism
""" 
a = 10
b = 20
print(a+b)

a = "kamesh"
b = "kumar"
print(a+b)



class Addition:
    def __init__(self,a):
        self.a = a

    def __add__(o1,o2):
        return o1.a + o2.a
    
    def __sub__(o1,o2):
        return o1.a - o2.a

o1 = Addition(10)
o2 = Addition(20)

print("Total : ",(o1+o2))
print("Difference : ",(o1-o2))

"""

#Abstract Base Class

"""
from abc import ABC ,abstractmethod

class Bank(ABC):

    @abstractmethod
    def loan(self): pass
    
    @abstractmethod
    def credit(self): pass
    
    @abstractmethod
    def debit(self): pass

class HDFC(Bank):

    def loan(self):
        print("We can Provide 7.5% interest Loan")

    def credit(self):
        print("HDFC Provide Credit")

    def debit(self):
        print("HDFC Provide Debit")

o = HDFC()
o.loan()
o.debit()
o.credit()

"""


