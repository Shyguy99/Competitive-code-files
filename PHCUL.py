from math import sqrt
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    n,m,k=list(map(int,input().split()))
    nn=list(map(int,input().split()))
    mm=list(map(int,input().split()))
    kk=list(map(int,input().split()))
    d=1000000000000000000000000
    dd=100000000000000000000000
    for i in range(0,len(nn),2):
        d1=sqrt(pow(x-nn[i],2)+pow(y-nn[i+1],2))
        for j in range(0,len(mm),2):
            d2=sqrt(pow(nn[i]-mm[j],2)+pow(nn[i+1]-mm[j+1],2))+d1
            if d2<d:
                d=d2
                x1=mm[j]
                y1=mm[j+1]
    for i in range(0,len(mm),2):
        d1=sqrt(pow(x-mm[i],2)+pow(y-mm[i+1],2))
        for j in range(0,len(nn),2):
            d2=sqrt(pow(nn[j]-mm[i],2)+pow(nn[j+1]-mm[i+1],2))+d1
            if d2<d:
                d=d2
                x1 = nn[j]
                y1 = nn[j+1]
    fin=1000000000000000000000
    for l in range(0,len(kk),2):
        dis=sqrt(pow(x1-kk[l], 2) + pow(y1- kk[l + 1],2))
        if dis<fin:
            fin=dis
    print(fin+d)

