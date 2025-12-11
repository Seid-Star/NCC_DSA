n,t=map(int,input().split())
arr=list(map(int,input().split()))
t=t-1
crim=0
for d in range(n):
    L=t-d
    R=t+d
    if L>= 0 and R<n:
        if arr[L]==1 and arr[R] == 1:
            if L==R:
                crim=crim+1
            else:
                crim=crim+2
    elif L>=0:
        crim=crim+arr[L]
    elif R<n:
        crim=crim+arr[R]
print(crim)