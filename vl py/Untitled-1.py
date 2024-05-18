# """
# #type casting

# a=10.0
# print(a)
# print(type(a))
# b=int(a)
# print(type(b))

#constructor #type convertion 
# integer #float #str

# a =int(input("enter your A:"))
# b =int(input("enter your B :"))
# c=a+b
# print("total :"+str(c))



#String and string function

# s="kamesh kumar"
# print(type(s))
# print(s)
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.count("k"))
# print(s.endswith("ar"))
# print(s.find("m"))
# print(s.find("m",5))
# print(s.replace("k","K"))

# a="kamesh"
# print("IS UPPER :",a.isupper())
# print("IS LOWER :",a.islower())
# print("IsALPHANUMERIC:",a.isalnum())
# print("IsALPHA:",a.isalpha())

# s="he\nis\ngood"
# print(s)
# print(s.splitlines())
# print(s.splitlines(True))
# s="  kamesh    "
# print(s.split(" ,"))
# print(len(s))
# print(len(s.strip()))#letter only display
# print(len(s.lstrip()))
# print(len(s.rstrip()))
# s = '01 04-2024'
# print(s.partition('-'))




#string manipulation 
#arry slicing

# s="kamesh kumar"
# print(s[:5])
# print(s[::-1]) #reserves print


#bitwise operater
"""
& and - 
| or
^ xor
~ not
<< zero fill left shift
>> signed right shift
"""

# a=25
# b=45
# print(a&b)
# print(a|b) 
# print(a^b)
# print(~25) #-26
# print(a<<2)


#identity operator

# is is not
"""
a = [1,2]
b = [1,2]
c = a
print(id(a))
print(id(c))
print(id(b))
print(a is b)
"""



#membership operator
#in not in
"""
a = [10,25,35,45,88]
print(22  in a)
print(45 not in  a)
"""


#if else condition

# n=int(input("Enter your number:"))
# if n%2==0:
#     print(n,"is a even number")
# else:
#     print(n, "is a odd number")

# name=input("enter your name:")
# age=int(input("enter your age:"))
# if age>=18:
#     print(name,"age is",age,"voter is eligible")
# else:
#     print(name,"age is",age,"voter is not eligible")


#elif Statement in python
"""
dates =int(input("enter the dates :"))
if dates==0:
    print("good No fiine")
elif dates>=1 and dates<=5:
    print("fine amount :",dates*0.5)
elif dates>=5 and dates<=10:
    print("fine amount :",dates*1)
elif dates>=10 and dates<=30:
    print("fine amount :",dates*5)
else:
    print("Membership cancel")
"""

#Nested if statement in python

# mark1 = int(input("Enter your mark1:"))
# mark2 = int(input("Enter your mark2:"))
# mark3 = int(input("Enter your mark3:"))
# total=mark1+mark2+mark3
# average=total/3.0
# print("Total",total)
# print("average",average)
# if mark1>=35 and mark2>=35 and mark3>35:
#     print("RESULT :PASSS")
#     if average>=90 and average<=100:
#         print("Grade : A")
#     elif average>=80 and average<=89:
#         print("Grade : B")
#     elif average>=70 and average<=79:
#         print("Grade : C")
#     else:
#         print("Grade : D")
# else:
#     print("RESULT :FAILL")
#     print("Grade : NO Grade")


#While loop Statements
#while  
"""
i=1
while i<=10:
    print(i,end=" ")
    i+=1
"""
#odd number

# i=1
# while i<=20 :
#     print(i)
#     i+=2 #i=i+3


# continue Statements

# i=1
# while i<=20:                              
#     if i%2==0:
#         i=i+1
#         continue
#     print(i)
#     i+=1


#Break Statement
"""
i=1
while i<=20:
    if i==19:
        break
    print(i)
    i+=1
"""

#Range
"""
print(list(range(5)))
"""

#For loop
"""
for i in range(1,20,2):
    print(i)

for i in range(5):
    a=int(input("Enter number A :"))
    b=int(input("Enter number B :"))
    print("Result :",a+b)
"""

#nested  For Loop Statements
"""
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print("")
"""
# a-z => 97-122 chr(i)
# A-Z => 65-90
"""  
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end=" ")
    print(" ")
"""
#While Else & For Else
"""
i=1
while i<=5:
    if i==4:
        break
    print(i)
    i=+1
else:
    print("Loop Completed")
"""
"""
for i in range(1,21):
    if i==5:
        break
    print(i)
else:
    print("Loop Completed")
"""

#List in Python
"""
Sequence type
Mutable -> easy we can change value
"""
"""
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
"""
#python Slicing
"""
print(a[0])
print(a[-1])
print(a[::-1])
"""
print("---------------------------------")
"""
a=[1,True,"kamesh",2.5,[1,2,3,4,5]]
print(type(a))
print(a[0],"this type is" ,type(a[0])) 
print(a[4],"this type is",type(a[4]))
print(a[4][2])

"""
#list function
"""
a=[10,25,35,45]
print(a)
a.clear()
print(a)

#copy

a=[10,25,35,45]
b=a.copy()
print(b)



#count

a = [10,25,35,45,25,4,25]
print(a.count(25))


#index
print(a.index(25))

#len
print(len(a))

#max
print(max(a))

#min
print(min(a))



#pop

a.pop(0) #remove Elements using index
print(a)
"""

#remove
"""
a = [10,25,35,45,25,4,25]
a.remove(25) #values 
print(a)

print("---------------------------------")
"""

#append

"""
name=["kamesh"]
name.append("karthik")
name.append("jovithika")
name.append("krithika")
print(name)
"""


#extend
"""

name2=["makka","pirate","hari"]
name.extend(name2)
print(name)
"""

#insert

"""
name.insert(0,"suriya")
print(name)

print("---------------------------------")

print(list(range(5)))
print(list("Kamesh kumar"))
"""

#sort asscending order
"""

a=[10,50,100,25,85]
a.sort()
print(a)

c=["orange","apple","zebra"]
c.sort()
print(c)
"""

#length
"""

c.sort(key=len)
print(c)

c.reverse()
print(c)

"""



#resverse descending order
"""
a.reverse()
a.sort(reverse=True)
print(a)

"""


#Tuple in Python
"""
Immutable
Surrounded by Round brackets ()
"""
"""
a=(1,2.5,True,"Ram")
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[-1])
print(a[0:2])

b=list(a)
print(a)
print(type(a))
b.append("kamesh")
print(b)
a=tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)

if "kamesh" in a:
    print("kamesh is found")
else:
    print("not found Kamesh")

print(len(a))

#delete
# del a
# print(a)

#concatenate


a = (1,2,3,4,5,7)
b = (6,7,8,9,10)
c=a+b
print(c)
print(a.count(7))


#nested tuples

a = (1,2,3,4,5,)
b = (6,7,8,9,10)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[1][0])
print(min(a))
print(max(b))

x=("kamesh",)*10
print(x)
"""

#set 
#unordered
#index don't do  we dont do correction in name
#{}->using the cyrly bracket

"""
name = {"kamesh","sam","ravi"}
print(name)

#access value using for loop
for i in name:
    print(i)

# Adding New Element
name.add("sara")
print(name)

#update Another Set of data
a = {"kumar","sundar","suresh"}
name.update(a)
print(name)

#Remove
name.remove("sara")
print(name)

#discard
name.discard("Kamesh")
print(name)

#pop
name.pop()
print(name)


#clear
name.clear()
print(name)

# del
# del name
# print(name)



name = {"Ram","Sam","Ravi","Kumar","Sundar","Suresh","Ram"} # union values only show in output
print(name)

#union
a = {1,2,3,4,5}
b = {"a","b","c","d"}
c = a.union(b)
print(c)

#update
a.update(b)
print(a)

# a = {1,2,3}
# b = {5,6,7}

#intersection


c=a.intersection(b) #common value show
print(c)
a.intersection_update(b)
print(a)


#symmetric_Difference

c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)


#isdisjoint

c = a.isdisjoint(b)
print(c)

#issubset
c = a.issubset(b) #this is want to be same value in a and b
print(c)

#issuperset
c = a.issuperset(b)
print(c)


#Dictionaries and its Function 

#Dont give duliplicate value in dict


user = {
    "name":"Kamesh","age":25,"Marriage status":False
}
print(type(user))
print(user["name"])
print(user["age"])

print(user.values())
print(user.keys())
print(user.items())
print(user.get('age'))

for i in user:
    print(i)
    print(user[i])

for i in user.values():
    print(i)

for i in user.keys():
    print(i)

for i,j in user.items():
    print(i,j)

if "gender" in user:
    print("Present")
else:
    print("No")

#changing Values

user.update({"gender":"male"})
print(user)
user["age"] = 35
print(user)

#remove
user.pop("age")
print(user)

#clear
user.clear()
print(user)


users={
    "user1": {
        "name":"Kamesh",
        "age":25,
        "Marriage status":False
    },
"user2": {
        "name":"Kumar",
        "age":23,
        "Marriage status":False
    }

}

print(users)

"""

#functions
"""
def welcome():
    print("welcome graet kirikalan magic show")

welcome()
welcome()
"""
# No return type without arguments function in python
# No return type with arguments function in python
# Return type without arguments function in python
# Return type with arguments function in python

#Arbitrary Arguments Function in Python(*)
"""
def Class_1(*students):
    print(students)
    for i in students:
        print(i)

Class_1("kames h","sam","raja","sara")

"""
#Keyword Arguments Function
"""
def message(name,age):
    print(name,"age is :",age)

message(age=25,name="kamesh")
"""
#Arbitrary Keyword Arguments in Python(**)
"""
def bioData(**data):
    print(data)
bioData(name="kamesh kumar",age=23,gender="Male")

"""
#Default Parameter
"""
def user(name,city="chennai"):
    print(name,"is from ",city)
user("kamesh","madras")
user("kumar")

"""

#Passing a list as an Argument in function 
"""

def total(marks):
    return sum(marks)
print("total:",total([55,75,80,95,47]))

"""

#Recursive Function

#1*2*3*4*5 =120
"""
def factorial(x):
    if x==1:
        return 1
    else:
        return (x *factorial(x - 1))
    
print("Factorial :",factorial(5))

"""

# 5 * factorial(5-1)
# 5*4 * factorial(4)
# 5*4*3 * factorial(3)
# 5*4*3*2 * factorial(2)
# 5*4*3*2*1
# 120

#Lambda
"""
c=lambda a:a+50
print(c(5))


c=lambda a,b:a+b
print(c(5,20))

"""
                                                             
#Date Time Functions

"""
import datetime as dt
current_date = dt.date.today()
print("current date :",current_date)


new = dt.date(2021,10,25)
print(new)
print(new.year)
print(new.day)
print(new.month)

print("----------------------------")

a = dt.datetime.now()
print(a.minute)
print(a.microsecond)
print(a.second)
print(a.hour)

print("-----------------")
current = dt.datetime.now()
new_year = dt.datetime(2025,1,1)
difference = new_year - current
print(difference)

print("-----------------")
current = dt.datetime.now()
print(current)
s = current.strftime("%a %b %d %I")
print(s)

"""
#math -->package
"""
import math as m
print(m.sqrt(10))     
print(m.ceil(1.55555)) #2
print(m.floor(1.55555)) #1
print(m.factorial(5))  #1*2*3*4*5
print(m.fabs(-10))  #positive value only show
print(m.pow(2,5))   #Expontional
print(m.log2(2))
print(m.log10(2))
print(m.pi)
print(m.e)

"""
#try block in python


try:
    a = 10/0
except Exception as e:
    print(e)



#try else block in python


try:
    a = 10/20
except Exception as e:
    print(e)
else:
    print("A value: ",a)


#Finally Block 


try:
    a = 10/20
except Exception as e:
    print(e)
else:
    print("A value: ",a)
finally:
    print("Thank You")



#Type of Exceptions

print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

#Nameerror Exception
try:
    print(b)
except NameError as e:
    print("A is not Defined")

#ZeroDivisionerror
try:
    print(10/0)
except ZeroDivisionError as e:
    print("denominator cant be zero")

#ValueError
try:
    a=int("joe")
except ValueError as e:
    print("Please enter Number Only")

#IndexError
try:
    a = [10,20,30,40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")

#filenotfound
try:
    f=open("test.txt")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())


#handing Multiple Exception 

try:
    print(10/25)
    b=[10,20,30,40]
    print(b[1])
except ZeroDivisionError as e:
    print("Denominator can't be zero")
except IndexError as e:
    print("Invalid error")




