

''''
graph=[[0, 0,0,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,1,0],
        [0,1,0,1,0,0,0,0,1],
        [0,1,1,0,1,0,1,0,0],
        [0,0,0,1,0,1,0,0,0],
        [0,0,0,0,1,0,1,0,0],
        [0,0,0,1,0,1,0,1,0],
        [0,1,0,0,0,0,1,0,1],
        [0,0,1,0,0,0,0,1,0]]
x=[0,0,0,0,0,0,0,0,0]
def nextvalue(k):
    while (1):
        x[k]=((x[k]+1)%(n+1))
        if (x[k]==0):
            return
        if(k==1):
           return
        j1=0
        if ((graph[x[k-1]][x[k]]) ):
            for j in range(1,k):
                j1=j
                if(x[j]==x[k]):
                   break
            if ( (j1==k-1) ):
                if( (k<n) or ((k==n) and graph[x[n]][x[1]])):
                   return
def hamlitonian(k):
    while(1):
        nextvalue(k)
        if(x[k]==0):
           return
        if((k==n)and(graph[x[n]][x[1]])):
            x.append(x[1]) 
            print(x[1:])
            x.pop()
        else:
            hamlitonian(k+1)
print("2213711058039")
print("\n HAMILTONIAN CYCLE (Backtracking)")
n=8
k=1
hamlitonian(k)
'''






COST=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
A=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
A1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
STATUS=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
PATH=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
pathstatus=2
def sml(a,b):
    if (a<=b):
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
                (pathstatus, A1[i][j])=sml(A[i][j],(A[i][k]+A[k][j]))
                if(pathstatus==1):
                   PATH[i][j]=k
                   STATUS[i][j]=1
        for i in range(0,n):
            for j in range(0,n):
                A[i][j]=A1[i][j]
print("2213711058039")
print("ALL PAIR SHORTEST PATH ALGORITHM-Dynamic Programming")
n=4
for i in range(0,n):
    for j in range (0,n):
        COST[i][j]=int(input("Enter Cost Matrix")) 
        A[i][j]=COST[i][j]
print("The Given COST MATRIX:",A)
APSP(A,4)
print("Final COST MATRIX:",A)
print("PATH TO ALL PAIR OF NODES")
for i in range(0,n):
    for j in range(0,n):
        if(STATUS[i][j]==1):
           print("Path from vertex",i+1,"to",j+1,"is:",i+1,"->",PATH[i][j]+1,"->",j+1)
        else:
             print("Path from vertex ",i+1,"to",j+1,"is:",i+1,"->",j+1)
