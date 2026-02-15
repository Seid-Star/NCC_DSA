a=int(input())
for x in range(a):
    b=input().strip()
    c=input().strip()
    d=input().strip()
    e=input().strip()
    f=input().strip()
    g=input().strip()
    h=input().strip()
    i=input().strip()
    j=input().strip()
    k=input().strip()
    Total=0
    B=b.count('X')
    C=c.count('X')
    if c[0]=='X':
        B+=1
        C=C-1
    if c[9]=='X':
        B+=1
        C=C-1
    D=d.count('X')
    if d[0]=='X':
        B+=1
        D=D-1
    if d[9]=='X':
        B+=1
        D=D-1
    if d[1]=='X':
        C=C+1
        D=D-1
    if d[8]=='X':
        C=C+1
        D=D-1
    E=e.count('X')
    if e[0]=='X':
        B+=1
        E=E-1
    if e[9]=='X':
        B+=1
        E=E-1
    if e[1]=='X':
        C=C+1
        E=E-1
    if e[8]=='X':
        C=C+1
        E=E-1
    if e[2]=='X':
        D=D+1
        E=E-1
    if e[7]=='X':
        D=D+1
        E=E-1
    F=f.count('X')
    if f[0]=='X':
        B+=1
        F=F-1
    if f[9]=='X':
        B+=1
        F=F-1
    if f[1]=='X':
        C=C+1
        F=F-1
    if f[8]=='X':
        C=C+1
        F=F-1
    if f[2]=='X':
        D=D+1
        F=F-1
    if f[7]=='X':
        D=D+1
        F=F-1
    if f[3]=='X':
        E=E+1
        F=F-1
    if f[6]=='X':
        E=E+1
        F=F-1
    G=g.count('X')
    if g[0]=='X':
        B+=1
        G=G-1
    if g[9]=='X':
        B+=1
        G=G-1
    if g[1]=='X':
        C=C+1
        G=G-1
    if g[8]=='X':
        C=C+1
        G=G-1
    if g[2]=='X':
        D=D+1
        G=G-1
    if g[7]=='X':
        D=D+1
        G=G-1
    if g[3]=='X':
        E=E+1
        G=G-1
    if g[6]=='X':
        E=E+1
        G=G-1
    H=h.count('X')
    if h[0]=='X':
        B+=1
        H=H-1
    if h[9]=='X':
        B+=1
        H=H-1
    if h[1]=='X':
        C=C+1
        H=H-1
    if h[8]=='X':
        C=C+1
        H=H-1
    if h[2]=='X':
        D=D+1
        H=H-1
    if h[7]=='X':
        D=D+1
        H=H-1
    I=i.count('X')
    if i[0]=='X':
        B+=1
        I=I-1
    if i[9]=='X':
        B+=1
        I=I-1
    if i[1]=='X':
        C=C+1
        I=I-1
    if i[8]=='X':
        C=C+1
        I=I-1
    J=j.count('X')
    if j[0]=='X':
        B+=1
        J=J-1
    if j[9]=='X':
        B+=1
        J=J-1
    K=k.count('X')
    Total=B+C*2+D*3+E*4+F*5+G*5+H*4+I*3+J*2+K
    print(Total)
    
    
    
    
    
    
        
    

