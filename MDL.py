for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=min(a)
    c=max(a)
    if a.index(b)>a.index(c):
        print(c,b)
    else:
        print(b,c)