from itertools import combinations
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    comb=combinations(a,k)
    su=sum(a)
    o=-1
    for k in comb:
        if sum(k)<su:
            su=sum(k)
            o=0
        elif sum(k)==su:
            o+=1
    print(o+1)