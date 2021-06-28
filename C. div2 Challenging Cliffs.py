for _ in range(int(input())):
    n=int(input())

    a=list(map(int,input().split()))

    a.sort()
    if n>2:
        minn=10000000000000
        for j in range(n-1):
            if a[j+1]-a[j]<minn:
                k1=a[j]
                k2=a[j+1]
                minn=k2-k1
        a.remove(k1)
        a.remove(k2)
        a.sort()

        fin=[]
        j=0
        i=0
        tr=0
        fin1=[]
        while tr<n-2:
            if a[tr]<=k1:
                fin1.append(a[tr])
            else:
                fin.append(a[tr])
            tr+=1
        fi=[k1]+fin+fin1+[k2]
        print(*fi)
    else:
        print(*a)

