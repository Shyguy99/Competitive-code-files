from math import factorial as fact
for _ in range(int(input())):
    n=int(input())
    s=input()
    ca=0
    a=[]
    cv=0
    v=[]
    vo=['A','E','I','O','U']
    dicv=dict()
    dica=dict()
    for i in s:
        if i in vo:
              cv+=1
              dicv[i] = dicv.get(i, 0) + 1
        else:
            dica[i] = dica.get(i, 0) + 1
            ca+=1
    fc_cv=fact(cv)
    tv=1
    for j in dicv:
        tv*=fact(dicv[j])
    fc_cv=fc_cv/tv

    if cv!=0 and ca!=0:
        ca+=1
    fc_ca=fact(ca)
    ta=1
    for k in dica:
        ta*=fact(dica[k])

    fc_ca=fc_ca/ta
    print(int(fc_cv*fc_ca))
