for _ in range(int(input())):
    x,r,m=map(int,input().split())


    r=60*r
    m=60*m
    if r<=m:

        #k=((r-x)*2)+x
        k=(r/x)-1

        if k>=0:
            fin=x+((r//x)-1)*x*2
            s=r-(x+((r//x)-1)*x)
            fin+=2*s
        else:
           fin=r

        print(fin)
        if fin<=m:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
