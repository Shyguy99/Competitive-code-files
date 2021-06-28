def c(a):
    k = len(a)
    fin = 0
    fin += k * int(a[0])
    z = 9
    k-=1
    for i in range(1, len(a)):
        s = int(a[0]) * z*k
        z *= 10
        fin += s
        k-=1
    return fin
for _ in range(int(input())):
    a,b=map(str,input().split())

    k1=len(a)
    k2=len(b)


    fin1=0
    for p in range(k1):

        fin1+=c(a[p:])


    fin2=0
    for q in range(k2):
         fin2+=c(b[q:])

    print(fin2-fin1)



