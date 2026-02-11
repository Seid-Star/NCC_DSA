a=int(input())
for x in range(a):
    b=input().strip()
    c=len(b)-1
    arr=[]
    d=0
    for i in range(len(b)):
        e=b[d]+('0')*c
        if b[d]!='0':
            arr.append(e)
        d+=1
        c-=1
    print(len(arr))
    print(*arr)
