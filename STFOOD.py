from math import floor
for _ in range(int(input())):
    n=int(input())
    k=0
    for i in range(n):
        s,p,v=list(map(int,input().split()))
        m=floor(p/(s+1))*v
        print(m)
        if m>k:
            k=m
    print(k)  