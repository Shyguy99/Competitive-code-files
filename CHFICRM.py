for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    afive=0
    aten=0
    chk=0
    for i in a:
        k=i-5
        if i==5:
            afive+=1

        elif i==10:
            aten+=1
            if afive!=0:
                afive-=1
            else:
                chk=1
                break
        else:
            if aten!=0:
                aten-=1
            elif afive>1:
                afive-=2
            else:
                chk=1
                break
    if chk==1:
        print("NO")
    else:
        print("YES")
