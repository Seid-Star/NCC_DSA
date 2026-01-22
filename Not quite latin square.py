a=int(input())
for x in range(a):
    b=input().strip()
    c=input().strip()
    d=input().strip()
    G=list(b)
    M=list(c)
    U=list(d)
    count=0
    coun=0
    cou=0
    for i in G:
        if i=='A':
            count=count+1
        if i=='B':
            coun=coun+1
        if i=='C':
            cou=cou+1
    for y in M:
        if y=='A':
            count=count+1
        if y=='B':
            coun=coun+1
        if y=='C':
            cou=cou+1
    for z in U:
        if z=='A':
            count=count+1
        if z=='B':
            coun=coun+1
        if z=='C':
            cou=cou+1
    if count<3:
        print("A")
    elif coun<3:
        print("B")
    else:
        print("C")
    
