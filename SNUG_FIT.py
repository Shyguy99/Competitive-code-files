for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    su=0
    a.sort()
    b.sort()
    for i in range(n):
        o=n-1-i
        k=a[o]
        l=b[o]
        if k>l:
            su+=l
        elif l>k:
            su+=k
        else:
            su+=k

    print(su)    