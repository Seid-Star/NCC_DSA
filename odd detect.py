n=int(input())
for x in range(n):
    a,b,c=map(int,input().split())
    if a==b:
        print(c)
    elif b==c:
        print(a)
    else:
        print(b)        