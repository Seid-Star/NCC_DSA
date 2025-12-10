a=input()
arr=[]
A="."
B="-."
C="--"
D="0"
E="1"
F="2"
i=0
while i < len(a):
    if a[i] in A:
        arr.append(D)
        i=i+1
    else:
        sec=a[i:i+2]
        if sec==B:
            arr.append(E)
        elif sec==C:
            arr.append(F)
        i=i+2 
print("".join(arr))                