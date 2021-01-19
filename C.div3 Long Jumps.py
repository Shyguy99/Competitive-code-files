for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    su=[0]*(n+1)
    for j in range(n-1,-1,-1):
        if j+a[j]>n-1:
            su[j]=a[j]
        else:
          su[j]=a[j]+su[j+a[j]]
    print(max(su))