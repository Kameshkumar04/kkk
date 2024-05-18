
for i in "apple":
    print(i)
for i in range(5):
    print(i)
i=2
for i in range(20):
    print(i,'x',i,'=',i*2)

a=int(input("Enter Your Number"))
b=int(input("Enter Your Number"))
for i in range(a+1,b):
    print(i)

#Even number

for i in range(1,11):
    if(i%2==0):
        print(i)
        
#odd number
for i in range(1,11):
    if(i%3==0):
        print(i)

#count
count=0
for i in range(1,11):
    count=count+1
print(count)

#Even and Odd Count
a=int(input("Enter Your Number A : "))
b=int(input("Enter Your Number B : "))
e_count=0
o_count=0
for i in range(a,b):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print("even number :",e_count)
print("odd number :",o_count)

#count number Divisible by 3 and 5
t_count =0
for i in range(1,100):
    if(i%3==0 and i%5==0):
        t_count=t_count+1
print("3divisible:",t_count)

#5 natural number
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
1
#10 number input 10 number avg
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)
print(sum/10)

a=[]
print("Enter 10 Numbers")
for i in range(5):
    num=int(input("Enter number "+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)

#n terms of natural numbers
list=[1,2,3,4,5,6,7]
sum=0
for i in list:
    print(i,end="")
    sum=sum+i
print(sum)

love=[]
for i in range(7):
    purpose=int(input("Enter your number "+str(i+1),))
    love.append(purpose)
    sum=sum+i
print(love)
sum=0
for i in love:
    sum=sum+i
print(sum)

for i in range(1,6):
    print('number is :',i,'and cube of the', i ,'is :',i*i*i)

n=int(input())
for i in range (1,n):
    print("Number is : " + str(i) + "and the cube of " + str(i) + "is :" + str(i**3))



