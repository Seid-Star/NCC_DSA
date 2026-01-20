a=int(input())
if a%2==1:
    print(-1)
else:
    arr=[]
    for i in range(1,a+1,2):
        arr.append(i+1)
        arr.append(i)
    print(*arr)
