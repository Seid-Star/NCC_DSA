a=int(input())
for x in range(a):
    b,c,d,e=map(int,input().split())
    f=max(b,c,d)
    g=f-b
    h=f-c
    i=f-d
    j=g+h+i
    k=e-j
    if k%3==0 and k>=0:
        print("YES")
    else:
        print("NO")

        
        





