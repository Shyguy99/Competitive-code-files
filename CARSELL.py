for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    q=0
    su=0
    a.sort()
    a=a[::-1]
    for i in a:
        if (i-q)<=0:
            break
        else:
            su=su+(i-q)
        q+=1
    print(su%1000000007)