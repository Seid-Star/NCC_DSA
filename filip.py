a=list(map(str,input().split()))
if a[0][::-1]>a[1][::-1]:
    print(a[0][::-1])
else:
    print(a[1][::-1])