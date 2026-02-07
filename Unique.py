a=int(input())
for x in range(a):
    b=int(input())
    if b>45:
        print(-1)
        continue
    c=[]
    for i in range(9,0,-1):
        if b>=i:
            c.append(str(i))
            b=b-i
    c.sort()
    print(''.join(map(str,c)))
