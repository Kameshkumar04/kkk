"""
A=[]
n=int(input("\nEnter the values:" ))
for i in range(n):
  i=int(input("Enter the elements: "))
  A.append(i)
print(A)
def selectionsort(A,n,k):
  low=0
  up=n+1
  A.append(999)
  while True:
   j= partition (A,low,up)
   if(k==j):
      print("The Kth smallest element is")
      print(A[k])
      return
   elif(k<j):
      up=j
   else:
      low=j+1
def partition(A,m,p):
  v=A[m]
  i=m
  j=p
  while True:
    i=i+1
    while A[i]<=v:
      i=i+1
    while A[p]>v:
      p=p-1
    if i<p:
      temp=A[i]
      A[i]=A[p]
      A[p]=temp
    if i>=p:
      break
  A[m]=A[p]
  A[p]=v
  return p
print("Program for searching an element using selection sort")
k1=int(input("enter the Kth smallest element to be found"))
k=k1-1
print("The given elements")
print(A)
selectionsort (A,len(A)-1,k)



class Myclass:
  a=10
  b=20
  def add():
    sum=a+b
    print(sum)


#accesssing variable present inside myclass
class Myclass:
  a=10
  b=20
print("2213711058039")
print(Myclass.a)


#creating object
class Myclass:
  a=10
  b=20
  def add(self):
    sum=self.a+self.b
    print(sum)
ob=Myclass()
print("2213711058039")
print(ob.a)
print(ob.b)


#constructor
class Myclass:
  sum=0
  def __init__(self,a,b):
    self.sum=a+b
  def printsum(self):
    print("2213711058039")
    print("sum of a and b is:",self.sum)
ob=Myclass(22,15)
ob.printsum()

#single inheritance
class operations:
  a=10
  b=20
  def add(self):
    sum=self.a+self.b
    print("2213711058039")
    print("sum of a and b is:",sum)
class Myclass(operations):
  c=50
  d=10
  def sub(self):
    sub=self.c-self.d
    print("substraction of c & d is:",sub)
ob=Myclass()
ob.add()
ob.sub()


#multilevel inheritance
class addition:
  a=10
  b=20
  def add(self):
    sum=self.a+self.b
    print("2213711058039")
    print("sum of a and b is:",sum)
class subtraction(addition):
  def sub(self):
    sub=self.b-self.a
    print("substraction of a & b is:",sub)
class multiplication(subtraction):
  def mul(self):
    mul=self.a*self.b
    print("multiplication of a and b is:",mul)
ob=multiplication()
ob.add()
ob.sub()
ob.mul()



def maxmin(lb,ub,L):
  if lb==ub:
    return L[lb],L[ub]
  elif lb==ub-1:
    if L[lb]>L[ub]:
      return L[lb],L[ub]
    else:
      return L[ub],L[lb]
  else:
    mid=(lb+ub)//2
    gmax,gmin=maxmin(lb,mid,L)
    hmax,hmin=maxmin(mid+1,ub,L)
    fmax=max(gmax,hmax)
    fmin=min(gmin,hmin)
    return fmax,fmin
L=[18,10,25,1,15]
maxi,mini=maxmin(0,len(L)-1,L)
print("maximum:",maxi)
print("minimum:",mini) 


A=[]
n=int(input("enter the value"))
for i in range(n):
  i=int(input("enter the element"))
  A.append(i)
print(A)
def selectionsort(A,n,k):
  low=0
  up=n+1
  A.append(999)
  while True:
    j=partition(A,low,up)
    while k==j:
      print("the smallest kTH element:")
      print(A[k])
      return
    if k<j:
      low=j
    elif k>j:
    
      up=j+1
def partition(A,m,p):
  v=A[m]
  i=m
  j=p
  while True:
    i=i+1
    while A[i]<=v:
      i=i+1
    while A[p]>v:
      p=p-1
    if i<p:
      temp=A[i]
      A[i]=A[p]
      A[p]=temp
    if i>=p:
      break
  A[m]=A[p]
  A[p]=v
  return p
k1=int(input("the smallest kth elemement to be found"))
k=k1-1
print("the given element")
print(A)
selectionsort(A,len(A)-1,k)



tu=(23,'abc',45.6,(2,3),4)
print(tu)
print(tu[1])
print(tu[-1])
print(tu[1:3])
print(tu[:])
print(tu[2:])
print(tu[:2])


li=[23,2,9,90]
print(3 in li)
print(3 not in li)
li.reverse()
print(li)
li.sort()
print(li)

li=['a','b','c','b']
li.append('d')
print(li)


A=[]
n=int(input("enter the value"))
for i in range(n):
  i=int(input("enter the element"))
  A.append(i)
print(A)
def selectionsort(A,n,k):
  low=0
  up=n+1
  A.append(999)
  while True:
    j=partition(A,low,up)
    while(k==j):
      print("the smallest kth value")
      print(A[k])
      return
    if(k<j):
      up=j
    else:
      low=j+1
def partition(A,m,p):
  v=A[m]
  i=m
  j=p
  while True:
    i=i+1
    while A[i]<=v:
      i=i+1
    while A[p]>v:
      p=p-1
      if i<p:
        temp=A[i]
        A[i]=A[p]
        A[p]=temp
      elif i>=p:
        break
    A[m]=A[p]
    A[p]=v
    return p
k1=int(input("the smallest kth element to be found"))
k=k1-1
print("the given element")
print(A)
selectionsort(A,len(A)-1,k)

"""

def mergesort(A,low,high):
  if low<high:
    mid=(low+high)//2
    mergesort(A,low,mid)
    mergesort(A,mid+1,high)
    merge(A,low,mid,high)
def merge(A,low,mid,high):
  h=low
  i=ow
  j=mid+1
  while h<=mid and j<=high:
    if A[h]<A[j]:
      B[i]=A[h]
      h+=1
    elif A[j]<A[h]:
      B[i]=A[j]
      j+=1
    i+=1
  while h<=mid:
    B[i]=A[h]
    h+=1
    i+=1
  while j<=high:
    B[i]=A[j]
    j+=1
    i+=1
  for k in range(low,high+1):
    A[k]=B[k]
A=list(eval(input("enter the list:")))
B=[0]*len(A)
mergesort(A,0,len(A)-1)
print(A)






































