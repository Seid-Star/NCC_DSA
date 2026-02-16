a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    if b==2:
        print("YES")
    elif len(set(arr))==1:
        print("YES")
    elif len(set(arr))==2:
        brr=list(set(arr))
        A=arr.count(brr[0])
        B=arr.count(brr[1])
        C=abs(B-A)
        if C>1:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")

        
        
