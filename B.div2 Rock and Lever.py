import math
for _ in range(int(input())):
    n=int(input())

    a=list(map(int,input().split()))

    di=dict()
    for i in range(n):
        k=int(math.log2(a[i]))+1
        if k not in di:
            di[k]=1
        else:
            di[k]+=1
    fin=0
    for i in di:
        if di[i]>1:
            fin+=((di[i]-1)*di[i])//2
    print(fin)
