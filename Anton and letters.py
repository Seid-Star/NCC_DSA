a=input().strip('{}')
if a=="":
    print(0)
else:
    b=a.split(',')
    print(len(set(b)))


