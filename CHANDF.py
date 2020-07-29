for _ in range(int(input())):
    a,b,l,r=list(map(int,input().split()))
    aa=a
    bb=b
    rr=r
    if a<b:
        a=bin(a).replace("0b","")
        b=bin(b).replace("0b","")
    else:
        a=bin(bb).replace("0b","")
        b=bin(aa).replace("0b","")
    if l==0 and (r>=2*max(aa,bb) or aa<=rr<=bb):
        r=bin(r).replace("0b","")
        s=""
        for i in range(-1,-len(a)-1,-1):
            s+=str(int(a[i])|int(b[i]))
        s=s[::-1]
        chk=s[:]
        s=b[:i]+s
        kk=len(s)-len(r)
        if kk>=1:
           s=s[kk:]
        if int(s)>int(r):
            p=len(r)-len(a)
            pp=s[:p]
            w = list(pp[:])
            for z in range(-1,-len(pp)-1,-1):
                if pp[z]=='1':
                    w[z]='0'
                    if int("".join(w)+chk)<=int(r):
                        break
            for u in range(-1,z,-1):
                if pp[u]!=w[u]:
                    w[u]='1'
                    if int("".join(w)+chk)<=int(r):
                        continue
                    else:
                        w[u]='0'
                        break
            print(int("".join(w)+chk,2))
            print((aa&int("".join(w)+chk,2))*(bb&int("".join(w)+chk,2)))

        else:
            print(int(s,2))
            print((aa&int(s,2))*(bb&int(s,2)))
    else:
        t = 0
        fin = 0
        for i in range(l, rr + 1):
            s = (aa & i) * (bb & i)
            if s > t:
                t = s
                fin = i
        if t == 0:
            print(l)
        else:
            print(fin)



