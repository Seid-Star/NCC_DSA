d=float(input())
w=float(input())
k=int(input())
import math
Cc=d*math.pi
Ks=w*k
if Cc>=Ks:
    print("YES")
else:
    print("NO")