"""print("POWER STATUS")
print("POWER OFF \nPOWER ON")
status = input("Enter Power Status : ")
if status == "POWER OFF":
    print("INVERTER ON")
print("THANK YOU!!!")
"""
"""
def multiply(a, b):
    c = a * b
    print("Multiplication:", c)
a1 = int(input("enter the number :"))
b1 = int(input("enter the number :"))
    

multiply(a1,b1)
"""
"""
def kamesh():
    a=12
    b=4
    c=a//b
    return c
print(kamesh()+6)
"""
"""
print("student Record")
name = input("Enter the Name: ")
std = input("Enter the Standard : ")
mark1 = int(input("enter mark1:"))
mark2 = int(input("enter mark2:"))
mark3 = int(input("enter mark3:"))
total = mark1 + mark2 + mark3
avg = total / 3
print("------Record------")
print("NAME : ",name)
print("STANDARD : ",std)
print("maths , physcis,chemistry : ",mark1,"-",mark2,"-",mark3)
print("AVERAGE:",avg )
#validate Result
if mark1>=45 and mark2>=45 and mark3>=45:
    print("RESULT:PASS")
    if avg >80 and avg <=90:
        print("GRADE : A")
    elif avg>70 and avg<=80:
        print("GRADE :  B")
    elif avg>60 and avg<=70:
        print("GRADE :  C")
    else:
        print("GRADE : D")
else:
    print("RESULT : FAIL")
    print("GRADE : zero")
print("---------------")
print("THANK YOU!!!!!")
"""
"""

for i in range (6,0,-1):
    for j in range(i):
        print(" ",end="")
    for j in range(6,i,-1):
        print("*",end=" ")
    print("")

"""
"""
for i in "ABCDEFIJKLMNOPQRSTUVWXYZ":
    if i=="M":
        pass
    print("Alphabets:",i,end=" 33")
print("Thankyou!!!")
"""
my_tuple = (1, 'Hello', 3.14, True)
tuple_string = str(my_tuple)
print(type(tuple_string))