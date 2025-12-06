import bisect
a=int(input())
arr=list(map(int,input().split()))
arr.sort()
b=int(input())
for x in range(b):
    c=int(input())
    print(bisect.bisect_right(arr,c))