"""
def kamesh():
    a=89
    b=98
    c=a+b
    print(c)
kamesh()

def classs():
    a=int(input("Enter the value :  "))
    b=int(input("Enter the value :  "))
    c=a+b
    print(c)
classs()

def cbi(a,b):
    c=a+b
    print(c)
a1= int(input("Enter the value :  "))
b1= int(input("Enter the value : "))
cbi(a1,b1)



def kai():
    a=4
    b=5
    c=a+b
    return(c)
print(kai()+5)

def details(ID,NAME,AGE):
    print("IDENTIFY:",ID)
    print("NAMES:",NAME)
    print("AGES:",AGE)
details(26,4,"Ajay")

print("Power status")
print("power off \npower on")
status = input("Enter Power Status: ")
if status == "power off":
    print("Inverter on")
print("Thank you!!!")


print("Welcome to login Page")
username = input("Enter Username : ")
Password =(input("Enter Password : "))
if username == "Admin" and Password == "Admin@123":
    print("Welcome User")
else:
    print("Invalid")
print("Thank You!!!")


i=1
while i<=20:
    print("4","*",i,"=",i*4)
    i+=1

i=1
n=int(input("Enter the Table : "))
while i<=10:
    print(str(n)+"*"+str(i)+"="+str(i*n))
    i+=1
else:
    print("Program End")
"""
"""
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in "abcdefghijklmnopqrstuvwxyz":
    if i=="m":
        pass
    print("Alphabets", i)

for i in "abcdefghijklmnopqrstuvwxyz":
    if i=="m":
        break
    print("Alphabets", i)

for i in "abcdefghijklmnopqrstuvwxyz":
    if i=="m":
        continue
    print("Alphabets", i)

s = "Python Programming"
print(s.index('o'))
print(s.find("o"))

print(s[1:3])


a = "apple",2,3,"2+3j"
del a
print(a)
print(type(a))
"""
"""

a = ("kaka","akjs","aslk")
b = ("jhkj","jhiu","oiu")
age = (12,34,67,44)
result =zip (a,b,age)
print(tuple(result))

try:
    a=int(input("enter the value : "))
    b = int(input("enter the value : "))
    c= a/b
except ZeroDivisionError as e1:
    print("Divide by Zero is not Possible")
except Exception as e:
    print("Error:",e)
else:
    print("Result: ",c)
finally:
    print("Thank You !!!")
"""

import datetime
obj=datetime.datetime.now()
print(obj)
print(obj.year)
print(obj.month)
print(obj.hour)
print(obj.minute)
print(obj.second)
print(obj.microsecond)

def add(a:sum(a)
print(value(10,20,30,40,50))

