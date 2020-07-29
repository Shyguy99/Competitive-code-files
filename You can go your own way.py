for z in range(1,int(input())+1):
    m=int(input())-1
    s=input()
    a=0
    b=0
    fir=[[0,0]]
    x=0
    y=0
    for i in s:
        if i=='S':
            a+=1
        else:
            b+=1
        fir.append([a,b])
    g=0
    p=0
    fin=""
    while x!=m or y!=m:
       ll=[x,y]
       if ll in fir:
            g=fir.index(ll)
            if p==0:
                if (fir[g+1][1]-fir[g][1]!=1):
                  y+=1
                  fin=fin+"E"
                  p=1
                else:
                  x+=1
                  fin=fin+"S"
                  p=0
            elif p==1:
                if (fir[g+1][0]-fir[g][0]!=1):
                  x+=1
                  fin=fin+"S"
                  p=0
                else:
                  y+=1
                  fin=fin+"E"
                  p=1
       elif p==0:
           y += 1
           fin = fin + "E"
           p = 1
       elif p==1:
           x+=1
           fin=fin+"S"
           p=0
    print("Case #{}: {}".format(z,fin))