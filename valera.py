n=int(input())
a=[input() for _ in range(n)]
b=a[0][0]
c=a[0][1]
if b==c:
    print("NO")
    exit()
ok=True
for i in range(n):
    for j in range(n):
        if i==j or i+j==n - 1:
            if a[i][j]!=b:
                ok=False
        else:
            if a[i][j]!=c:
                ok=False
if ok:
    print("YES")
else:
    print("NO")                    