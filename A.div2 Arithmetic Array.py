for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    su=sum(a)
    if su==n:
        print(0)
    elif su<n:
        print(1)
    else:
        k=su-n
        print(k)

