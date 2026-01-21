a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    ev=[]
    od=[]
    for x in arr:
        if x%2==0:
            ev.append(x)
        else:
            od.append(x)
    if sum(ev)>sum(od):
        print("YES")
    else:
        print("NO")
