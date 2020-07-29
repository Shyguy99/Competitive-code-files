for z in range(1, int(input()) + 1):
    n= list(map(int,input()))
    nn=len(n)

    s=[0]
    for i in n:
        k=i
        for j in range(len(s)-1,-1,-1):

            if s[j]==")":
                k-=1
            elif j!=len(s)-1 and s[j]!="(" and str(s[j]).isnumeric():
                break
            df=''
            if k==0:
                s.insert(j,str(i))
                break
        if k!=0:
            p=i
            l=""
            r=""
            for j in range(len(s) - 1, -1, -1):
                if s[j] == ")":
                    p -= 1
                if p==k or (str(s[j]).isnumeric() and j!=len(s)-1):
                    for o in range(k):
                        s.insert(j,")")
                        j=j+1
                    s.insert(j-k,str(i))
                    j=j+1
                    for o in range(k):
                        s.insert(j-1-k, "(")
                        j=j+1
                    break
    d=""
    for q in s:
        d=d+str(q)
    d=d[:-1]
    print("Case #{}: {} ".format(z,d))
