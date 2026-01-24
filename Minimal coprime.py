a=int(input())
for x in range(a):
    l,r=map(int,input().split())
    if l==1 and r==1 or l==0 and r==0:
        print(1)
    else:
        print(abs(l-r))
