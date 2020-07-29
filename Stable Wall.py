for z in range(1,int(input())+1):
    r,c=list(map(int,input().split()))
    a=[]
    t=set()
    af = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        q=input()
        a.append(list(a for a in q))
        for l in q:
            t.add(l)
    t=list(t)

    setin=[]
    res=[]
    for e in t:
       res=[]
       for x in range(r):
           res = res + [[x, p] for p, value in enumerate(a[x]) if value == e]
       setin.append(res)

    def one(ss):
        global af
        for i in ss:
            af[int(i[0])][int(i[1])]=1
    def zero(ss):
        global af
        for i in ss:
            af[i[0]][i[1]]=0
    def chk():
        global af
        ch=1
        for i in range(r):
            for j in range(c):
                if i!=r-1:
                    if af[i][j]==1 and af[i+1][j]!=1:
                        ch=0
                        break
            if ch==0:
                 break
        return ch
    g=0
    fin=""
    i=0
    re=0
    while len(t)!=0:
        one(setin[i])
        if chk()==0:
             g+=1
             if g==len(t):
                 re=1
                 break
             zero(setin[i])
             i+=1
        else:
            fin+=t[i]
            t.remove(t[i])
            setin.remove(setin[i])
            i=0
            g=0
    if re==1:
       print("Case #{}: {}".format(z,-1))
    else:
       print("Case #{}: {}".format(z, fin))