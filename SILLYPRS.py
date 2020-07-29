for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    b=b[::-1]
    s=0
    for i in range(n):
        s=(a[i]+b[i])/2

    print(s)
