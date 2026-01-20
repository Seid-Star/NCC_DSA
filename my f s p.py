a=int(input())
for x in range(a):
    arr=list(map(int,input().split()))
    arr.sort()
    print(*arr)