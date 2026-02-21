a=int(input())
for x in range(a):
    b=input().strip()
    c=int(b[0])-1
    d=c*10
    e=len(b)
    arr=[]
    for i in range(1,e+1):
        arr.append(i)
    f=sum(arr)
    g=f+d
    print(g)
    
    
