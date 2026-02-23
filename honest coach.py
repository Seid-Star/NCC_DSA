a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    brr=[]
    if b==len(set(arr)):
        for i in range(1,b):
            brr.append(arr[i]-arr[i-1])
        print(min(brr))
    else:
        print(0)
        





