for _ in range(int(input())):
    n=int(input())
    q=[]
    for i in range(n):
        q.append(input())
    fin=0
    for j in range(10):
        p=""
        for l in q:
            p=p+l[j]
        if p.count('1')%2!=0:
            fin+=1
    print(fin)