for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    coun=0
    o=0
    it=[751,751,751,751,751]
    for i in range(len(a)):
        if a[i]<min(it):
            coun+=1
        it[o]=a[i]
        o+=1
        if o>4:
            o=0
    print(coun)
