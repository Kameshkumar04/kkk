GRAPH=[[0,1,0,1,0,0,0,0,1],
       [0,1,1,0,1,0,1,0,0],
       [0,0,0,1,0,1,0,0,0],
       [0,0,0,0,1,0,1,0,0],
       [0,0,0,1,0,1,0,1,0],
       [0,1,0,0,0,0,1,0,1],
       [0,0,1,0,0,0,0,1,0]]
X=[0,0,0,0,0,0,0,0,0]
def NEXTVALUE(k):
    while (1):
        X[k]=((X[k]+1)%(n+1))
        if (X[k]==0):
            return
        if (k==1):
            return
        j1=0
        if ((GRAPH[X[k-1]][X[k]])):
            for j in range(1,k):
                j1 = j
                if (X[j]==X[k]):
                    break
            if ((j1==k-1)):
                if((k<n) or ((k==n) and GRAPH[X[n]][X[1]])):
                    return
def HAMILTONIAN(k):
    while (1):
        NEXTVALUE(k)
        if (X[k]==0):
            return
        if ((k==n) and (GRAPH[X[n]][X[1]])):
            X.append(X[1])
            print(X[1:])
            X.pop()
        else:
            HAMILTONIAN(k+1)
print("\n HAMILTONIAN CYCLE (BACKTRACKING)")
n=8
k=1
HAMILTONIAN(k)


