for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(n):
        k=0
        t=a[i+1:]
        w=t.count(a[i])
        fi=n-(i+1)-w
        b.append(fi)
    print(*b)


