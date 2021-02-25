from collections import defaultdict

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    di=defaultdict()
    for i in a:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    maxx=0
    for l in di:
          maxx=max(maxx,di[l])
    print(maxx)