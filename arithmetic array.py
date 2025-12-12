n=int(input())
for x in range(n):
    a=int(input())
    arr=list(map(int,input().split()))
    if sum(arr)==a:
        print("0")
    elif sum(arr)<a:
        print("1")    
    else:
        print(sum(arr)-a)