a=int(input())
for x in range(a):
    b=int(input())
    bx=2
    bk=0
    for i in range(2,b+1):
        k=b//i
        s=i*k*(k+1)//2
        if s>bk:
            bk=s
            bx=i
    print(bx)
        
        
