a=int(input())
count=0
for x in range(a):
    arr=list(map(int,input().split()))
    if sum(arr)>=2:
        count=count+1
print(count)
