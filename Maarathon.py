n=int(input())
for x in range(n):
    arr=list(map(int,input().split()))
    count=0
    for i in arr:
        if i>arr[0]:
            count+=1
    print(count)
