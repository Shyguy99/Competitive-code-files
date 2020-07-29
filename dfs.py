n=int(input())
a=list(map(str,input().split()))
c=1
le=[]
lo=[]
for i in a:
    ia=int(i[0])
    ib=int(i[1])
    ic=int(i[2])
    imin=min(ia,ib,ic)
    imax=max(ia,ib,ic)
    ifin=str(imin*7 + imax*11)
    ifin=ifin[-2:]

    if c%2==0:
       le.append(ifin[0])
    else:
        lo.append(ifin[0])
    c+=1
le.sort()
lo.sort()
t=1
pair=0
for o in range(len(le)-1):
    if le[o]==le[o+1]:
        t+=1
    else:
        if t==2:
            pair+=1
        elif t>2:
            print(t)
            pair+=2
        t=1
if t==2:
            pair+=1
elif t>2:
            pair+=2
t=1
for o in range(len(lo)-1):
    if lo[o]==lo[o+1]:
        t+=1
    else:
        if t==2:
            pair+=1
        elif t>2:
            pair+=2
        t=1
if t==2:
            pair+=1
elif t>2:
            print(t)
            pair+=2

print(pair)
