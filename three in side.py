a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    print(sum(arr)-(b-1))
