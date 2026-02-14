a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=[]
    if b==1:
        print(max(2*(abs(c-arr[0])),arr[0]))
    else:
        for i in range(len(arr)-1):
            brr.append(abs(arr[i]-arr[i+1]))
        brr.append(2*((abs(max(arr)-c))))
        print(max((max(brr),min(arr))))
    
