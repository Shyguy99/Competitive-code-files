for z in range(1,int(input())+1):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    c=0
    res = [i for i, value in enumerate(l) if value == k]
    o=0
    for s in res:
        try:
            if l[s+(k-1)]==1:
                t=k
                for i in range(s,s+k):
                    if l[i]!=t:
                        break
                    t-=1
                if t==0:
                    c+=1
        except:
            break

    print("Case #{}: {}".format(z,c))