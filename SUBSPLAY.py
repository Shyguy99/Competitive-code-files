for _ in range(int(input())):
    n=int(input())
    a=input()
    p=[]
    for i in range(n):
        ss=''
        for j in range(i,n):
            ss=ss+a[j]
            p.append(ss)
    mi=0
    print(p)
    for l in p:
        if p.count(l)>1:
            if len(l)>mi:
                mi=len(l)
    print(mi)

#wrong