n=int(input())
a=list(map(int,input().split()))
t=0
c=0
for i in a:
    if i !=-1:
        t=t+i
        c=c+1
r=t/c        
print(r)