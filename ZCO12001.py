n=int(input())
a=list(map(int,input().split()))
maxi=0
c_maxi=0
maxl=0
c_maxl=0
li=[1]
for i in range(n):
    c_maxl+=1
    if a[i]==1:
        c_maxi+=1
        if c_maxi>maxi:
            maxi=c_maxi
            pmax=i+1
    else:
        c_maxi-=1

    if c_maxi==0:
        li.append(i+2)
        if c_maxl>maxl:
            maxl=c_maxl
            pmaxl=li[-2]
        c_maxl=0
print(maxi,pmax,maxl,pmaxl)

