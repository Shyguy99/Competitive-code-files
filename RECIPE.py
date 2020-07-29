for _ in range(int(input())):
    m=list(map(int,input().split()))
    n=m[0]
    m=m[1:]
    l=min(m)
    c=0
    for k in range(1,l+1):
        temp=[]
        for g in range(n):
            if m[g]%k!=0:
                break
            temp.append(int(m[g]/k))
        if len(temp)==n:
            fin=temp[:]
    print(*fin)

