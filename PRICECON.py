for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    s1=sum(a)
    s2=0
    for i in a:
        if i>k:
            s2+=k
        else:
            s2+=i
    print(s1-s2)