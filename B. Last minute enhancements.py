for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    con=dict()
    fin=0
    for i in a:
        if i not in con:
            fin+=1
            con[i]=1
        elif con[i]==1:
            if i+1 not in con:
                fin+=1
                con[i+1]=1
    print(fin)
