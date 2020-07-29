for _ in range(int(input())):
    d=[]
    n=int(input())
    for i in range(n):
        d.append(list(map(int,input().split())))
    l_outer=[]
    for k in range(n-1):
        l_inner=[]
        for l in range(k+1,n):
            l_inner.append(min(abs(d[l][0]-d[k][0]),abs(d[l][1]-d[k][1])))
        l_outer.append(l_inner)

    check1=[]
    check2=[]
    for c in range(1,n+1):
        check1.append(c)

    fin_list=[]
    minf=10000
    for ii in l_outer:
        for jj in ii:
            if jj<minf:
               minf=jj
               fir1=l_outer.index(ii)+1
               fir2=l_outer[fir1-1].index(jj)+fir1+1
    fin_list.append(fir1)
    fin_list.append(fir2)
    check1.remove(fir1)
    check1.remove(fir2)
    chl=len(check1)

    for w in range(chl):
        mins = 10000
        for y in check1:
                if y < fin_list[-1]:
                    z = y - 1
                    x = fin_list[-1]-y-1
                    a = l_outer[z][x]
                elif y > fin_list[-1]:
                    z=fin_list[-1]-1
                    x=y-fin_list[-1]-1
                    a=l_outer[z][x]
                if a<mins:
                   mins=a
                   o=y
        fin_list.append(o)
        check1.remove(o)

    res=fin_list[0]
    for i in range(1,len(fin_list)):
        res=res^fin_list[i]

    print(res)
#easy way--->
# for _ in range(int(input())):
#     n=int(input())
#     d=[]
#     for i in range(n):
#        d.append(list(map(int,input().split())))
#     res=1
#     for j in range(2,n+1):
#         res=res^j
#     print(res)


