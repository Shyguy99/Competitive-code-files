import math
t=int(input())
for _ in range(t):
    n=int(input())
    i=int(math.log(n,2))
    if i>11:
        i=11
    count=0
    r=0
    while i>=0:
        k=2**i
        while(r<=n):
            r+=k
            if r==n:
                count+=1
                break
            elif r>n:
                r-=k
                break
            count += 1
        if r==n:
            break
        i-=1
    print(count)

