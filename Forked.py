n=int(input())
for x in range(n):
    a,b=map(int,input().split())
    kx,ky=map(int,input().split())
    qx,qy=map(int,input().split())
    d={(a,b),(a,-b),(-a,b),(-a,-b),(b,a),(b,-a),(-b,-a),(-b,a)}
    e=set()
    for x,y in d:
        e.add((kx+x,ky+y))
    f=0
    for x,y in d:
        if (qx+x,qy+y) in e:
            f=f+1
    print(f)

    
        
    

