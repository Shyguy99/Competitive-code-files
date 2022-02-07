import math

for _ in range(int(input())):
    n,k=map(int,input().split())


    l=math.log2(k+1)
    a=[]
    f=1
    for i in range(math.ceil(l)):
        a.append(f)
        f=f*n

    i=0
    ex=0
    while k!=0:

        if k & 1:
            ex+=a[i]
        k=k>>1
        i+=1

    print(ex%1000000007)
