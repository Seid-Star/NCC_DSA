a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    freq={}
    d=-1
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
        if freq[i]>=3:
            d=i
            break
    print(d)
    


