n=int(input())
bri=input()
bro=input()
ar=bri.count('r')
br=bro.count('r')
if ar==br:
    print(0)
else:
    am=bri.count('m')
    bm=bro.count('m')
    fin=0
    if ar>br:
        s=ar-br
        c='r'
    else:
        s=am-bm
        c='m'
    k=-1
    t=0
    while k>=-n:

        if bri[k]!=c:
                fin+=1
                k-=1
        else:
            if t!=s-1:
                 fin+=1
                 t+=1
                 k-=1
            else:
                fin+=1
                break
    print(fin)