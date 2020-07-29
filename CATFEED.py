#aaaa
for _ in range(int(input())):
    n=int(input())
    p = []
    for z in range(n):
        p.append(list(map(int,input().split())))
    a=0
    b=0
    for q in p:
        if q[0]==1 or q[1]==q[2]:
            a=q[1]
            b=q[2]
            print("YES")
        else:
            if q[1]<a<=q[2]:
                a=q[2]
                b=q[1]
                print("YES")
            elif q[1]<b<=q[2] :
                b=q[2]
                a=q[1]
                print("YES")
            elif  q[1]>=a>q[2]:
                a = q[1]
                b=q[2]
                print("YES")
            elif q[1]>=b>q[2]:
                b = q[1]
                a = q[2]
                print("YES")

            else:
                print("NO")
