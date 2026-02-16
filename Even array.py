a=int(input())
for x in range(a):
    b=int(input())
    count=0
    coun=0
    arr=list(map(int,input().split()))
    for i in range(b):
        if i%2!=arr[i]%2:
            if i%2==0:
                count+=1
            else:
                coun+=1
    if coun==count:
        print(count)
    else:
        print(-1)
        
