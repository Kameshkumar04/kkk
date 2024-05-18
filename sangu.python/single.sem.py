
cost=[[0,0,0],[0,0,0],[0,0,0]]
A=[[0,0,0],[0,0,0],[0,0,0]]
A1=[[0,0,0],[0,0,0],[0,0,0]]
STATUS=[[0,0,0],[0,0,0],[0,0,0]]
PATH=[[0,0,0],[0,0,0],[0,0,0]]
pathstatus=2
def sml(a,b):
    if(a<=b):
       pathstatus=0
       min1=a
    else:
       pathstatus=1
       min1=b
    return(pathstatus,min1)
def APSP(A,n):
  for k in range(0,n):
     for i in range(0,n):
        for j in range(0,n):
          (pathstatus,A1[i][j])=sml(A[i][j],(A[i][k]+A[k][j]))
          if(pathstatus==1):
            PATH[i][j]=k
            STATUS[i][j]=1
     for i in range(0,n):
        for j in range(0,n):
          A[i][j]=A1[i][j]
print("all pair shortest path")
n=3
for i in range(0,n):
  for j in range(0,n):
     cost[i][j]=int(input("enter the cost matrix:"))
     A[i][j]=cost[i][j]
print("the given cost matrix",A)
APSP(A,3)
print("final cost matrix",A)
print("path from the source")
for i in range(0,n):
 for j in range(0,n):
  if(STATUS[i][j]==1):
    print("path from the vertex",i+1,"to",j+1,"is",i+1,"->",PATH[i][j]+1,"->",j+1)
  else:
    print("path from the vertex",i+1,"to",j+1,"is",i+1,"->",j+1)
    


              
