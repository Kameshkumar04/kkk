print('2213711058039')
x=[0,0,0,0,0]
def PLACE(k):
    for i in range(1,k):
        if ((x[i]==x[k])or (abs(x[i]-x[k])==abs(i-k))):
            return(False)
    return(True)
def NQUEENS(n):
    print('solution set')
    x[1]=0
    k=1
    while(k>0):
        x[k]=x[k]+1
        while((x[k]<=n) and (not PLACE(k))):
            x[k]=x[k]+1
        if(x[k]<=n):
            if(k==n):
                print('x=',x[1:])
            else:
                k=k+1
                x[k]=0
        else:
            k=k-1
print('N-QUEEN PROBLEM (back tracking)')
NQUEENS(4)
