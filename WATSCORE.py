for _ in range(int(input())):
    n=int(input())
    a=[0]*8
    for i in range(n):
        p,s=list(map(int,input().split()))
        if p<9:
            if a[p-1]<s:
                a[p-1]=s
    print(sum(a))

