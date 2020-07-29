for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(str,input().split())))
    a.sort()
    p=a[n-1][0]
    pp=a[n-1][1]
    if p!="-1":
        to=int(pp,int(p))
        c=[]
        for t in a:
            if t[0]=="-1":
                q=0
                b=1
                try:
                    e=int(t[1])
                    for z in t[1]:
                        if int(z)>b:
                            b=int(z)
                except ValueError:
                    b=15
                for l in range(b+1,37):
                    if int(t[1],l)==to:
                        q=1
                c.append(q)
        c.sort()
        if 0 in c or c==[]:
            print("-1")
        else:
            print(to)
    else:
        print("-1")




