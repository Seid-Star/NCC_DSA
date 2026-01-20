s,n=map(int,input().split())
d=[]
for x in range(n):
    a,b=map(int,input().split())
    d.append((a,b))
d.sort()
for a,b in d:
         if s>a:
             s=s+b
         else:
             print("NO")
             break
else:
    print("YES")
