for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cap=int(input())
    con=[]
    pg=0
    for i in a:
        if i not in con:
            pg+=1
            if len(con)<cap:
                con.append(i)
            else:
               con.pop(0)
               con.append(i)
        else:
           con.remove(i)
           con.append(i)
    print(pg)