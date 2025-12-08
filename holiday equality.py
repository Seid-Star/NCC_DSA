n=input()
arr=list(map(int,input().split()))
current=0
b=max(arr)
for x in arr:
    c=b-x
    current=current+c
print(current)   
                