a=int(input())
for x in range(a):
    b,c,d=map(int,input().split())
    e=b
    f=c
    while c!=0:
        b,c=c,b%c
    g=b
    if e//g<=d and f//g<=d:
        print(1)
    else:
        print(2)
