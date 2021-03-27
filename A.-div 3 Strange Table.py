import math

for _ in range(int(input())):
    n,m,x=map(int,input().split())

    r=math.floor(x/n)

    p=(x-(n*r))
    if p!=0:
        r+=1
    else:
       p=n

    s=((p-1)*m)+r
    print(s)

