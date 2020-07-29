for _ in range(int(input())):
    n=int(input())
    c=o=d=e=h=f=0
    for i in range(n):
        s=input()
        for j in s:
            if j=='c':
                c+=1
            elif j=='o':
                o+=1
            elif j=='d':
                d+=1
            elif j=='e':
                e+=1
            elif j=='h':
                h+=1
            elif j=='f':
                f+=1
    c=c//2
    e=e//2
    print(min(c,o,d,e,h,f))
