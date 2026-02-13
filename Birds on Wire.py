a=int(input())
arr=list(map(int,input().split()))
b=int(input())
for x in range(b):
    c,d=map(int,input().split())
    if a==1:
        print(0)
        exit()
    while b>0:
        if c==1:
            arr[1]=arr[1]+(arr[0]-d)
            arr[0]=0
            b=b-1
        elif c==a:
            arr[a-2]=arr[a-2]+d-1
            arr[a-1]=0
            b=b-1
        else:
            arr[c]=arr[c]+(arr[c-1]-d)
            arr[c-2]=arr[c-2]+d-1
            arr[c-1]=0
            b=b-1
        break
for i in arr:
    print(i)
    
    
    
        
        
    
