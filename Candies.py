a,b=map(int,input().split())
arr=[]
if a%b==0:
    for i in range(b):
        arr.append(a//b)
    print(*arr)
else:
    c=a//b
    for x in range(b-(a%b)):
        arr.append(c)
    for y in range(a%b):
        arr.append(c+1)
    print(*arr)           