n=int(input())
count=0
for i in range(n):
    a,b,c=map(int,input().split())
    z=a+b+c
    if z>=2:
        count=count+1
print(count)        