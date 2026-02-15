a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    d=True
    arr=[]
    for i in range(len(c)):
        if i==0:
            arr.append(c[i])
        else:
            if c[i]!=c[i-1]:
                if c[i] in arr:
                    d=False
                    break
                arr.append(c[i])
    if d:
        print("YES")
    else:
        print("NO")

    
 
