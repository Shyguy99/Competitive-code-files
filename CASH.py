for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    o=sum(a)
    print(o%k)