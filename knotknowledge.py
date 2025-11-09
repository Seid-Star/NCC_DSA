a=int(input())
b=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in b:
    if i not in d:
        print(i)
        break
    
