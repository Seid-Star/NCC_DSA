a=int(input())
arr=[]
if a%2==0:
    print(a//2)
    for x in range(a//2):
        arr.append(2)
    print(*arr)
else:
    print(a//2)
    for x in range(a//2):
        arr.append(2)
    arr[-1]=3
    print(*arr)
    
