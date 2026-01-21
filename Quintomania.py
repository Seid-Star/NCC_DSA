    a=int(input())
    for x in range(a):
        b=int(input())
        arr=list(map(int,input().split()))
        c=True
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])!=5 and abs(arr[i]-arr[i+1])!=7:
                c=False
                break
        if c:
            print("YES")
        else:
            print("NO")
