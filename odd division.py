n=int(input())
for x in range(n):
    a=int(input())
    while a%2==0:
        a=a//2
    if a>1:
        print("YES")
    else:
        print("NO")        
        