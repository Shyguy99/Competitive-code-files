
for _ in range(int(input())):
    n,q=list(map(int,input().split()))
    b=list(map(int,input().split()))
    p = []
    for __ in range(q):
        q=list(map(int,input().split()))
        i1=q[0]-1
        i2=q[1]-1
        if (i1%2==0 and i2%2==0) or( i1%2!=0 and i2%2!=0):
            print("UNKNOWN")
        else:
            j1=min(i1,i2)
            j2=max(i1,i2)
            mid=int((j2-1+j1)/2)
            summ=0
            c=mid
            d=mid
            ss=[b[mid]]
            while c!=j1 and d!=(j2-1):
                c-=1
                d+=1
                summ=b[c]+b[d]
                ss.append(summ)
            while len(ss)!=1:
                l=ss[1]-ss[0]
                ss.remove(ss[0])
                ss.remove(ss[0])
                ss.insert(0,l)
            print(ss[0])


