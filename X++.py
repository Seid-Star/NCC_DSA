a=int(input())
x=0
for i in range(a):
    s=input().strip()
    if "++" in s:
        x=x+1
    else:
        x=x-1   
print(x)        
    