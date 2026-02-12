a=int(input())
arr=list(map(int,input().split()))
b=0
c=0
for i in arr:
    if i==-1:
        if c==0:
            b=b+1
        else:
            c=c+i
    else:
        c=c+i
print(b)
