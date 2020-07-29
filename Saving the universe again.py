for z in range(1,int(input())+1):
    tot, pr = list(map(str, input().split()))
    tot = int(tot)
    global dam
    def damc():
        dam = 0
        p = 1
        for i in pr:
            if i == 'C':
                p = p * 2
            if i == 'S':
                dam = dam + p
        return dam
    damm=damc()
    count=0
    if damm<=tot:
        print("Case #{}: {}".format(z,0))
    else:
        while True:
            j=len(pr)-2
            while j>=0:
                if pr[j]=='C' and pr[j+1]=='S':
                    pr=pr[:j]+'S'+pr[j+1:]
                    pr=pr[:j+1]+'C'+pr[j+2:]
                    count+=1
                    break
                j-=1
            damm = damc()
            if damm<=tot:
                print("Case #{}: {}".format(z,count))
                break
            elif j==-1:
                print("Case #{}: {}".format(z,"IMPOSSIBLE"))
                break

