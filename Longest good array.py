import math
a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d=c-b
    e=(1+math.sqrt(1+8*d))//2
    print(int(e))
        
        
    
