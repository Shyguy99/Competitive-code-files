for z in range(1,int(input())+1):
    n,q=list(map(int,input().split()))
    a=list(map(int,input().split()))
    summ=0
    for i in range(q):
        o,l,r=list(map(str,input().split()))
        if o=='Q':
            t=0
            tt=0
            for j in range(int(l)-1,int(r)):
                    t=t+ (((-1)**(tt))*a[j]*(tt+1))
                    tt+=1
            print(t)
            summ=summ+t
        else:
            a[int(l)-1]=int(r)
    print("Case #{}: {}".format(z,summ))









