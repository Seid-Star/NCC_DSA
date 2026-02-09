a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    if b%c==0:
        print(0)
    elif c>b:
        print(c-b)
    else:
        print(c-(b%c))
