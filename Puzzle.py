a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
c=float('inf')
for i in range(b-a+1):
    c=min(c,arr[i+a-1]-arr[i])
print(c)
