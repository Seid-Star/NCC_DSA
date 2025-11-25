n,k=map(int,input().split())
sc=list(map(int,input().split()))
count=0
ksc=sc[k-1]
for i in sc:
    if i>=ksc and i>0:
        count=count+1
print(count)       