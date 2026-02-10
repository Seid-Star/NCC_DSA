a,b=map(int,input().split())
for x in range(a):
    if x%2==0:
        print('#'*b)
    elif x%4==1:
        print('.'*(b-1)+'#')
    else:
        print('#'+'.'*(b-1))
