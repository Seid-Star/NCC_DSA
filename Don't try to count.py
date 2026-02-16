a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d=input().strip()
    e=input().strip()
    count=0
    while len(d)<=50:
        if e in d:
            print(count)
            break
        d=d+d
        count+=1    
    else:
        print(-1)
        
        


        
        
    
    
    
