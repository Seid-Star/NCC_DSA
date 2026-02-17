a=int(input())
for x in range(a):
    b,c,d=map(int,input().split())
    brr=[1]*b
    crr=[]
    e=b//2
    if d==1 and c==2:
        if b%2!=0:
            print("NO")
        else:
            print("YES")
            for i in range(e):
                crr.append(2)
            print(len(crr))
            print(*crr)           
    elif d==1 and c==1:
        print("NO")
    else:
        if d!=1:
            print("YES")
            print(len(brr))
            print(*brr)
        else:
            if b%2==0:
                for i in range(e):
                    crr.append(2)
            else:
                for i in range(e):
                    crr.append(2)
                crr[-1]=3
            print("YES")
            print(len(crr))
            print(*crr)

            
                
            
            
        
        

