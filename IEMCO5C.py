from math import gcd
n,q,k=list(map(int,input().split()))
tt=[]
for i in range(n):
    l,r=list(map(int,input().split()))
    tt.append([l,int((((r-l)/k)+1))])
fin=0
for qq in range(q):
    h=int(input())
    su = 0
    for z in range(len(tt)):
        su=su+tt[z][1]
        if su>=h:
            x=tt[z][1]-(su-h)-1
            fin=fin+tt[z][0]+(x*k)
            break
g=gcd(fin,q)
print(str(int(fin/g))+"/"+str(int(q/g)))