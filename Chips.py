a=int(input())
arr=list(map(int,input().split()))
count=0
coun=0
for i in arr:
    if i%2==0:
        count=count+1
    else:
        coun=coun+1
print(min(count,coun))
