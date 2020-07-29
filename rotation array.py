for _ in range(int(input())):
    n,d=list(map(int,input().split()))
    a=list(map(int,input().split()))
    k=[]
    for i in range(d,n):
        k.append(a[i])
    for j in range(d):
        k.append(a[j])
    print(k)