def solution(l):
    k = []
    i = 0
    z=0
    def done(l, i, k,z ):
        global c
        for r in range(i+1,len(l)):
            if l[r]%l[i]==0:
                if z<2:
                  done(l,r,k+[l[i]],z+1)
                else:
                   break
        if len(k)>1:
           c=c+1
    for o in range(len(l)-2):
        done(l, o, k,z)
    return c
c = 0
