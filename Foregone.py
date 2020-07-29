for z in range(1,int(input())+1):
    n=int(input())
    a=0
    b=n
    for i in range(int(n/2)+1):
        b=b-1
        a=a+1
        l1= [int(x) for x in str(b)]
        l2= [int(y) for y in str(a)]
        s1=""
        s2=""
        if 4 not in l1 and 4 not in l2:
            for p in l1:
                s1=s1+str(p)
            for q in l2:
                s2=s2+str(q)
            print("Case #{}: {} {}".format(z,int(s1),int(s2)))
            break

