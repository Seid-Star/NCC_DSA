a=int(input())
arr=[]
if a%2==1:
    print(-1)
else:
    for x in range(1,a+1):
        arr.append(x)
    for i in range(0,len(arr)-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    print(*arr)
