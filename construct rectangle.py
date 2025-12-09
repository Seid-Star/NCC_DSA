n=int(input())
for x in range(n):
    a,b,c=sorted(map(int,input().split()))
    if a==b and c%2==0:
        print("YES")
    elif b==c and a%2==0:
        print("YES")
    elif c==a+b:
        print("YES")
    else:
        print("NO")