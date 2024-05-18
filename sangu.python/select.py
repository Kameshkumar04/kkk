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

