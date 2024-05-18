'''
cost=[[0,1,3,100,100],[100,0,100,100,6],[100,100,0,4,2],[100,5,100,0,1],[100,100,100,100,0]]
DIST=[0,0,0,0,0]
s=[0,0,0,0,0]
path=[0,0,0,0,0]
path1=[0,0,0,0,0]
pvt1=[0,0,0,0,0]
pathstatus=2
def sml(a,b):
    if a<=b:
        pathstatus=0
        min1=a
    else:
        pathstatus=1
        min1=b
    return(pathstatus,min1)
def choose_u(v,s):
    min=100
    index=0
    for i in range(1,n):
        if(s[i]==0):
             if(DIST[i]<min):
                min=DIST[i]
                indexu=i
    return(indexu)
v=0
n=5
for i in range(0,n):
    s[i]=0
    DIST[i]=cost[v][i]
    path[i]=v
s[v]=1
DIST[v]=0
for i in range(1,n):
    u=choose_u(v,s)
    s[u]=1
    for w in range(0,n):
        if s[w]==0:
            pathstatus,DIST[w]=sml(DIST[w],(DIST[u]+cost[u][w]))
            if pathstatus==1:
                path[w]=u
print("source vertex",v+1)
print("final cost matrix",DIST)
    

A=[99,7,12,100,2,25,3,999]

def quicksort(A,p,q):
  if p<q:
     j=q+1
     jl=partition(A,p,j)
     quicksort(A,p,jl-1)
     quicksort(A,jl+1,q)
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
    if(i<p):
       temp=A[i]
       A[i]=A[p]
       A[p]=temp
    if i>=p:
        break
  A[m]=A[p]
  A[p]=v
  return p
print("quicksort")
print("the given element:",A)
for k in range(0,len(A)):
    print(A[k])
quicksort(A,0,len(A)-2)
print("after sorting the element")
for k in range(0,len(A)-0):
    print(A[k])
        


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
   if(k==j):
      print("the kth smallest element is")
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
    if(i<p):
       temp=A[i]
       A[i]=A[p]
       A[p]=temp
    if i>=p:
        break
  A[m]=A[p]
  A[p]=v
  return p
print("selection sortt")
k1=int(input("enter the kth smallest element"))
k=k1-1
print("the given element")
print(A)
selectionsort(A,len(A)-1,k)
'''
           
    
x=[0,0,0,0,0,0]
def PLACE(k):
  for i in range(1,k):
    if(x[i]==x[k]) or (abs(x[i]-x[k])==abs(i-k)):
        return(False)
  return(True)
def nqueens(n):
  print("solution set")
  x[1]=0
  k=1
  while(k>0):
    x[k]=x[k]+1
    while(x[k]<=n) and (not PLACE(k)):
       x[k]=x[k]+1
    if(x[k]<=n):
      if(k==n):
        print("x=",x[1:])
      else:
        k=k+1
        x[k]=0
    else:
       k=k-1
print("n quuen program")
nqueens(5)
       
           
       
      
    































