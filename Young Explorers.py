for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    c=0
    p=1
    for i in range(n):
        if l[i]<=p:
            c+=1
            p=p-l[i]+1
        else:
            p+=1
    print(c)