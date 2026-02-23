a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    count=0
    arr=[]
    for i in range(3,b+1):
        arr.append(i)
        if len(arr)==c:
            count+=1
            arr=[]
        elif i==b:
            count+=1
            break
    print(count+1)
        
    


