for z in range(1, int(input()) + 1):
    n = int(input())
    a = []
    su = 0
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for j in range(len(a)):
        su = su + a[j][j]
    rr=0
    cc=0
    for k in range(len(a)):
        k1=[]
        k2=[]
        for l in range(len(a)):
            k1.append(a[k][l])
            k2.append(a[l][k])
        k1.sort()
        k2.sort()
        if list(set(k1))!=k1:
            rr+=1
        if list(set(k2))!=k2:
            cc+=1
    print("Case #{}: {} {} {}".format(z, su, rr,cc))
