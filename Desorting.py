a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))    
    if arr!=sorted(arr):
        print(0)
    elif b==1:
        print(0)
    elif arr[-1]==arr[-2]:
        print(1)
    else:
        g=float('inf')
        for i in range(len(arr)-1):
            f=(arr[i+1]-arr[i])
            h=f//2+1
            g=min(g,h)
        print(g)
