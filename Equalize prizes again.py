a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    c=sum(arr)
    print((c+b-1)//b)
