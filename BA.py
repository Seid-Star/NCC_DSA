for x in range(5):
    arr=list(map(int,input().split()))
    for i in range(5):
        if arr[i]==1:
            a=x+1
            b=i+1
print(abs(a-3)+abs(b-3))
