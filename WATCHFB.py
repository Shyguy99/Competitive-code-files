for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    l=list(range(1,n+1))
    o=0
    tt=l[:]
    for i in a:
        if i in tt:
            tt.remove(i)
        else:
            o=1
        if tt==[]:
            tt=l[:]
    if o==0:
        print("YES")
    else:
        print("NO")