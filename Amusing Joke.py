a=input().strip()
b=input().strip()
c=input().strip()
d=a+b
if len(c)==len(d) and sorted(d)==sorted(c):
    print("YES")
else:
    print("NO")
