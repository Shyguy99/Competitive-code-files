for z in range(1,int(input())+1):
    n=int(input())
    l1 = [int(x) for x in str(n)]
    l2=[]
    s1=""
    s2=""
    for i in range(len(l1)):
        if l1[i]==4:
            l2.append(2)
            l1[i]=2
        else:
            l2.append(0)
    for q in l1:
        s1=s1+str(q)
    for w in l2:
        s2=s2+str(w)
    print("Case #{}: {} {}".format(z,int(s1),int(s2)))
