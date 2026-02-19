a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    b=arr.count(-1)
    c=arr.count(0)
    count=0
    if b%2!=0:
        count+=2
    else:
        count+=0
    count+=c
    print(count)
