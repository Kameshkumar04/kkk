"""
mark=int(input())
if (mark>35):
    print("pass")
else:
    print("fail")

income=int(input("income:"))
if(income>7000):
    print("not Eligible")
else:
    print("scholarship")
#and
number=int(input())
if(number%3==0 and number%5==0):
    print("number is divisible by 3 and 5")
else:
    print("number is not divisible by 3 and 5")

#even
number=int(input())
if(number%2==0):
    print("even")
else:
    print("odd")
    
a =int(input("enter Your Number :"))
if (a<35):
     print("poor Students")
elif (a>35 and a<70):
    print("Average students")
else:
    print("Good Students")
    
#mini calculator

a=int(input("enter your number 1 :"))
b=int(input("enter your number 2 :"))
operation = input("add/sub/mul/div : ")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("invalid operation ")


score_percentage =int(input("Enter your Score"))

if (score_percentage >=70):
    Name =input("Enter your Name :" )
    dept = input("Enter Your Dept:" )
    city = input("enter your city:")
    print("You are Eligible")
else:
    print("You nor Eligible")



salary = int(input("salary:"))
age = int(input("age:"))
if(salary >=2000 or age<=25):
    loan=int(input("Get your loan amount : "))
    if(loan>5000):#nestedif
        print("maximum amount is 5000")
    else:
        print("You are eligible")
        print("transfer successfully")
else:
    print("your are not eligible")
    
"""
mark1=int(input("enter your mark1:"))
mark2=int(input("enter your mark2:"))
mark3=int(input("enter your mark3:"))
mark4=int(input("enter your mark4:"))
mark5=int(input("enter your mark5:"))
total=mark1+mark2+mark3+mark4+mark5
print(total)
avg=total/5
print(avg)
if(avg<35):
    print("additional class is required")
else:
    print("you are good to go")

      
