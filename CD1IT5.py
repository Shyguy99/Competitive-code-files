def finde(p ,z):
    if z>= 0:
        z,p=finde(z, a[z])
    return z,p


n,q=list(map(int,input().split()))
a=[-1]*(n+1)
for i in range(q):
        t,x,y=list(map(int,input().split()))
        if t==0:
            l,lp=finde(x,x)
            k,kp=finde(y,y)
            if lp!=kp:
                if abs(l)>abs(k):
                    a[lp] = l + k
                    a[kp] = lp
                else:
                    a[kp] = l + k
                    a[lp] = kp
        elif t==1:
            l, lp = finde(x,x)
            k, kp = finde(y,y)
            if lp==kp:
                print("Yes")
            else:
                print("No")

