A=[89,7,12,100,3,25,33,17]
B=[0,0,0,0,0,0,0,0]
low=0
high=0
def mergesort(A,low,high):
  if low<high:
    mid=(low+high)//2
    mergesort(A,low,mid)
    mergesort(A,mid+1,high)
    merge(A,low,mid,high)
def merge(A,low,mid,high):
  h=low
  i=low
  j=mid+1
  while h<=mid and j<=high:
    if A[h]<A[j]:
      B[i]=A[h]
      h+=1
    else:
      B[i]=A[j]
      j+=1
    i+=1
  if h<=mid:
    for k in range(j,high+1):
      B[i]=A[h]
      h+=1
      i+=1
  else:
    for k in range(h,mid+1):
      B[i]=A[j]
      j+=1
      i+=1
  for k in range(low,high+1):
    A[k]=B[k]
print("the given element")
for k in A:
  print(k)
mergesort(A,0,len(A)-1)
print("The given element after sorting")
for k in A:
  print(k)


"""
A=list(eval(input("enter the list:")))
B=[0]*len(A)
mergesort(A,0,len(A)-1)
print(A)





A=[99,7,12,100,2,25,3,999]
def quicksort(A,p,q):
  if p<q:
    j=q+1
    j1=partition(A,p,j)
    quicksort(A,p,j1-1)
    quicksort(A,j1+1,q)
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
print("the given element")
for k in range(0,len(A)-1):
  print(A[k])
quicksort(A,0,len(A)-2)
print("The given element after sorting")
for k in range(0,len(A)-1):
  print(A[k])
  
"""



