"""
def mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        L=a[0:mid]
        R=a[mid:]
        mergesort(L)
        mergesort(R)

        a.clear()
        while len(L)>0 and len(R)>0:
            if L[0]<=R[0]:
                a.append(L[0])
                L.pop(0)
            else:
                a.append(R[0])
                R.pop(0)
        for i in L:
            a.append(i)
        for i in R:
            a.append(i)
            
a=[]
n=int(input("enter the upper limit:"))
for i in range(0,n):
    a.append(int(input("enter the element:")))
print(a)
        



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
        fmin= min(gmin,hmin)
        return fmax,fmin
L=[2,4,6,7,9]
maxi,mini=maxmin(0,len(L)-1,L)
print("2213711058039","\n")
print("Maximum: ", maxi, "\n")
print("Minimum: ",mini)
"""


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
print("2213711058039","\n")
"""
A=list(eval(input("enter the list:")))
B=[0]*len(A)
mergesort(A,0,len(A)-1)
print(A)
"""
a=[]
n=int(input("enter the upper limit:"))
for i in range(0,n):
    a.append(int(input("enter the element:")))
print(a)