for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=a[-1]
    flag=0
    for i in range(2,n+2):
        p=n-i
        if a[p]<a[p+1]:
            s=a[p:]
            s.sort()
            ll=s[s.index(a[p])+1]
            lk=a[::-1]
            l=len(a)-1-lk.index(ll)
            temp=ll
            a[l]=a[p]
            a[p]=temp
            flag=1
            break
    g=a[p+1:]
    g.sort()
    h=a[:p+1]+g
    if flag==1:
        print(int("".join(map(str,h))))
    if flag==0:
        print(-1)